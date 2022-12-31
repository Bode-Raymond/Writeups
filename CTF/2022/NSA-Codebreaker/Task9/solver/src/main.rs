use aes::Aes128;
use aes::cipher::KeyInit;
use aes::cipher::BlockDecrypt;
use aes::cipher::generic_array::GenericArray;

fn main() {
    let block: [u8; 16] = [0x00, 0xf0, 0x2c, 0x46, 0xd5, 0x02, 0x7a, 0x70, 0xde, 0x09, 0x29, 0x0e, 0x2f, 0x72, 0x6d, 0x05];
    let mut key: [u8; 16] = [b'c', b'b', b'8', b'9', b'7', b'0', b'0', b'0', b'-', b'e', b'0', b'2', b'0', b'-', b'1', b'1'];
    let comp: [u8; 4] = [0x5f, 0x06, 0x80, 0x35];
    let chars: [u8; 16] = [b'0', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9', b'a', b'b', b'c', b'd', b'e', b'f'];
    let mut index: [usize; 16] = [12, 11, 8, 9, 7, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0];
    let mut block_copy: [u8; 16];
    let mut cipher;

    loop {
        loop {
            loop {
                loop {
                    loop {
                        loop {
                            loop {
                                loop {
                                    loop {
                                        loop {
                                            block_copy = block;
                                            
                                            cipher = Aes128::new(&GenericArray::from(key));
                                            cipher.decrypt_block((&mut block_copy).into());

                                            if block_copy[0..4] == comp {
                                                println!("Key Found: {}", std::str::from_utf8(&key).unwrap());
                                                std::process::exit(0);
                                            }

                                            index[7] = (index[7] + 1) % 16;
                                            key[7] = chars[index[7]];

                                            if key[7] == b'0' {break;}
                                        }
                                        index[6] = (index[6] + 1) % 16;
                                        key[6] = chars[index[6]];

                                        if key[6] == b'0' {break;}
                                    }
                                    index[5] = (index[5] + 1) % 16;
                                    key[5] = chars[index[5]];

                                    if key[5] == b'0' {break;}
                                }
                                index[4] = (index[4] + 1) % 16;
                                key[4] = chars[index[4]];

                                if key[4] == b'0' {break;}
                            }
                            index[3] = (index[3] + 1) % 16;
                            key[3] = chars[index[3]];

                            if key[3] == b'0' {break;}
                        }
                        index[2] = (index[2] + 1) % 16;
                        key[2] = chars[index[2]];

                        if key[2] == b'0' {break;}
                    }
                    index[1] = (index[1] + 1) % 16;
                    key[1] = chars[index[1]];

                    if key[1] == b'0' {break;}
                }
                index[0] = (index[0] + 1) % 16;
                key[0] = chars[index[0]];

                if key[0] == b'0' {break;}
            }
            index[12] = (index[12] + 1) % 16;
            key[12] = chars[index[12]];

            if key[12] == b'0' {break;}
        }
        index[11] = (index[11] + 1) % 16;
        key[11] = chars[index[11]];

        if key[11] == b'0' {break;}
    }
}
