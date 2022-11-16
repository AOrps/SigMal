package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"fmt"
	"io"
	"log"
	"os"
)

// https://gist.github.com/josephspurrier/12cc5ed76d2228a41ceb

func decrypt(file, _key string) string {
	// Byte array of the string
	ciphertext := []byte(file)

	// Key
	key := []byte(_key)

	// Create the AES cipher
	block, err := aes.NewCipher(key)
	if err != nil {
		panic(err)
	}

	// Before even testing the decryption,
	// if the text is too small, then it is incorrect
	if len(ciphertext) < aes.BlockSize {
		panic("Text is too short")
	}

	// Get the 16 byte IV
	iv := ciphertext[:aes.BlockSize]

	// Remove the IV from the ciphertext
	ciphertext = ciphertext[aes.BlockSize:]

	// Return a decrypted stream
	stream := cipher.NewCFBDecrypter(block, iv)

	// Decrypt bytes from ciphertext
	stream.XORKeyStream(ciphertext, ciphertext)

	return string(ciphertext)
}

func encrypt(file, _key string) string {
	// Byte array of the string
	plaintext := []byte(file)

	// Key
	key := []byte(_key)

	// Create the AES cipher
	block, err := aes.NewCipher(key)
	if err != nil {
		panic(err)
	}

	// Empty array of 16 + plaintext length
	// Include the IV at the beginning
	ciphertext := make([]byte, aes.BlockSize+len(plaintext))

	// Slice of first 16 bytes
	iv := ciphertext[:aes.BlockSize]

	// Write 16 rand bytes to fill iv
	if _, err := io.ReadFull(rand.Reader, iv); err != nil {
		panic(err)
	}

	// Return an encrypted stream
	stream := cipher.NewCFBEncrypter(block, iv)

	// Encrypt bytes from plaintext to ciphertext
	stream.XORKeyStream(ciphertext[aes.BlockSize:], plaintext)

	return string(ciphertext)
}

func main() {
	key := "keykeykeykeykeykeykeykeykeykeyye"
	s1 := encrypt("superlongpasswdpasswd", key)

	d1 := []byte(s1)

	err := os.WriteFile("ciphertext.txt", d1, 0777)
	if err != nil {
		log.Fatal(err)
	}

	file, err := os.ReadFile("ciphertext.txt")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Print("cipher: ")
	fmt.Println(string(file))

	s2 := decrypt(string(file), key)

	fmt.Print("text: ")
	fmt.Println(s2)
}
