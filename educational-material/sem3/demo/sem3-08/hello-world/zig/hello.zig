const std = @import("std");

pub fn main() void {
    std.debug.print("Hel{s}\n", .{"lo"});
}

