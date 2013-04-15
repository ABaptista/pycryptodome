# -*- coding: utf-8 -*-
#
# SelfTest/Hash/test_SHA3_512.py: Self-test for the SHA-3/512 hash function
#
# Written in 2013 by Fabrizio Tarizzo <fabrizio@fabriziotarizzo.org>
#
# ===================================================================
# The contents of this file are dedicated to the public domain.  To
# the extent that dedication to the public domain is not available,
# everyone is granted a worldwide, perpetual, royalty-free,
# non-exclusive license to exercise all rights associated with the
# contents of this file for any purpose whatsoever.
# No rights are reserved.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ===================================================================

"""Self-test suite for Crypto.Hash.SHA3_512"""

__revision__ = "$Id$"


# This is a list of (expected_result, input[, description]) tuples.
test_data = [
# Test vectors from ``Keccak: Known-answer and Monte Carlo test results'',
# Version 3.0, January 14, 2011 <http://keccak.noekeon.org/KeccakKAT-3.zip>
    ('0eab42de4c3ceb9235fc91acffe746b29c29a8c366b7c60e4e67c466f36a4304'
    +'c00fa9caf9d87976ba469bcbe06713b435f091ef2769fb160cdab33d3670680e',
     '',
     'Empty string'),
     
     
    ('8630c13cbd066ea74bbe7fe468fec1dee10edc1254fb4c1b7c5fd69b646e44160'
    +'b8ce01d05a0908ca790dfb080f4b513bc3b6225ece7a810371441a5ac666eb9',
     '\xcc',
     '1 byte message'),

    ('9a7688e31aaf40c15575fc58c6b39267aad3722e696e518a9945cf7f7c0fea84c'
    +'b3cb2e9f0384a6b5dc671ade7fb4d2b27011173f3eeeaf17cb451cf26542031',
     '\xde\x8f\x1b?\xaaKp@\xedEc\xc3\xb8\xe5\x98%1x\xe8~M\r\xf7'
    +'^O\xf2\xf2\xde\xddZ\x0b\xe0F',
     '33 bytes message'),

     ('aa52587d84586317028fb7d3c20892e0288bfe2feabd76d7f89155ffe9ccbf1a'
     +'09fa0ffb0553e83f79ae58bd30a35fa54892b6aba0093a012427ddab71cdf819',
      '\x94\xf7\xca\x8e\x1aT#LmS\xccsK\xb3\xd3\x15\x0c\x8b\xa8\xc5\xf8\x80'
     +'\xea\xb8\xd2_\xed\x13y:\x97\x01\xeb\xe3 P\x92\x86\xfd\x8eB.\x93\x1d'
     +'\x99\xc9\x8d\xa4\xdf~p\xaeD{\xab\x8c\xff\xd9#\x82\xd8\xa7w`\xa2Y\xfc'
     +'O\xbdr',
      '70 byte (block size - 2) message'),
     
     ('48fc282f37a3e1fb5df4d2da1f7197ec899ae573ca08df550e61ee847eeb1d24c'
     +'074ff46bcaee224ec7d8cea4256154f0c4d434e682834f6d827bfbdf75112f5',
      '\x13\xbd(\x11\xf6\xed+o\x04\xff8\x95\xac\xee\xd7\xbe\xf8\xdc\xd4^'
     +'\xb1!y\x1b\xc1\x94\xa0\xf8\x06 k\xff\xc3\xb9(\x1c+0\x8b\x1ar\x9c'
     +'\xe0\x08\x11\x9d\xd3\x06n\x93x\xac\xdc\xc5\n\x98\xa8. s\x88\x00'
     +'\xb6\xcd\xdb\xe5\xfe\x96\x94\xadm',
      '71 byte (block size - 1) message'),
     
     ('6b4b0f126863552a6f40f45e295dc79b9ba2a88ea7c3b2f607ac1a8431a97844'
     +'c2a7b664443fb23c05739df5494fe9824db80b7f3e67872142f17e2c5544e1ef',
      '\x1e\xed\x9c\xba\x17\x9a\x00\x9e\xc2\xecU\x08w=\xd3\x05G|\xa1\x17'
      +'\xe6\xd5i\xe6k_d\xc6\xbcd\x80\x1c\xe2Z\x84$\xceJ&\xd5u\xb8\xa6\xfb'
      +'\x10\xea\xd3\xfd\x19\x92\xed\xdd\xee\xc2\xeb\xe7\x15\r\xc9\x8fc'
      +'\xad\xc3#~\xf5{\x919z\xa8\xa7',
     '72 byte (block size) message'),

    ('e5d53e81866283179012d9239340b0cbfb8d7aebce0c824dc6653a652bb1b54e08'
    +'83991be2c3e39ad111a7b24e95daf6f7d9a379d884d64f9c2afd645e1db5e2',
     '\x94\xb7\xfa\x0b\xc1\xc4N\x94\x9b\x1dv\x17\xd3\x1bG \xcb\xe7\xcaW'
    +'\xc6\xfaO@\x94\xd4v\x15g\xe3\x89\xec\xc6Oih\xe4\x06M\xf7\r\xf86\xa4'
    +'}\x0cq36\xb5\x02\x8b5\x93\r)\xebz\x7f\x9aZ\xf9\xad\\\xf4At[\xae\xc9'
    +'\xbb\x01L\xee\xffZA\xba\\\x1c\xe0\x85\xfe\xb9\x80\xba\xb9\xcfy\xf2'
    +'\x15\x8e\x03\xef~c\xe2\x9c8\xd7\x81j\x84\xd4\xf7\x1e\x0fT\x8b\x7f\xc3'
    +'\x16\x08Z\xe3\x8a\x06\x0f\xf9\xb8\xde\xc3o\x91\xad\x9e\xbc\n[l3\x8c'
    +'\xbb\x8ffY\xd3B\xa2Ch\xcf',
     '142 byte (2*block size - 2) message'),

    ('5da83b7e221933cd67fa2af8c9934db74ce822212c99e0ee01f5220b4fe1e9b038'
    +'8e42e328a1d174e6368f5773853042543a9b493a94b625980b73df3f3fccbb',
     '\xea@\xe8<\xb1\x8b:$,\x1e\xccl\xcd\x0bxS\xa49\xda\xb2\xc5i\xcf\xc6\xdc'
     +'8\xa1\x9f\\\x90\xac\xbfv\xae\xf9\xea7B\xff;T\xef}6\xeb|\xe4\xff\x1c\x9a'
     +'\xb3\xbc\x11\x9c\xffk\xe9<\x03\xe2\x08x35\xc0\xab\x817\xbe[\x10\xcd\xc6'
     +'o\xf3\xf8\x9a\x1b\xdd\xc6\xa1\xee\xd7OPL\xber\x90i\x0b\xb2\x95\xa8r\xb9'
     +'\xe3\xfe,\xee\x9elg\xc4\x1d\xb8\xef\xd7\xd8c\xcf\x10\xf8@\xfea\x8ey6'
     +'\xda=\xca\\\xa6\xdf\x93?$\xf6\x95K\xa0\x80\x1a\x12\x94\xcd\x8d~f\xdf\xaf'
     +'\xec',
     '143 byte (2*block size - 1) message'),
     
    ('72de9184beb5c6a37ea2c395734d0d5412991a57cffcc13ff9b5fa0f2046ee87c61'
    +'811fe8ef2470239d5066c220173de5ebe41885ed8acae397fb395e6ca9aee',
     '\x15}[~E\x07\xf6m\x9a&tv\xd381\xe7\xbbv\x8dM\x04\xcc48\xda\x12\xf9\x01'
     +'\x02c\xea_\xca\xfb\xde%y\xdb/kX\xf9\x11\xd5\x93\xd5\xf7\x9f\xb0_\xe3'
     +'Yn?\xa8\x0f\xf2\xf7a\xd1\xb0\xe5p\x80\x05\\\x11\x8cS\xe5<\xdbc\x05Ra'
     +'\xd7\xc9\xb2\xb3\x9b\xd9\n\xcc2R\x0c\xbb\xdb\xda,O\xd8\x85m\xbc\xee'
     +'\x1712\xa2g\x91\x98\xda\xf80\x07\xa9\xb5\xc5\x15\x11\xaeIvly*)R\x03\x88'
     +'DN\xbe\xfe(%o\xb3=B`C\x9c\xbas\xa9G\x9e\xe0\x0cc',
     '144 byte (2*block size) message'),
     
    ('b678fa7655584970dedbbc73a16d7840935b104d06dcb468ddd9814d6cf443fa6f92'
    +'45824dbff3ab5fffef24b29cb2978796f37e7b49b1682d59f79e3c169e81',
     '\x83k4\xb5\x15Goa?\xe4G\xa4\xe0\xc3\xf3\xb8\xf2\t\x10\xac\x89\xa3\x97pU'
    +'\xc9`\xd2\xd5\xd2\xb7+\xd8\xac\xc7\x15\xa9\x03S!\xb8g\x03\xa4\x11\xdd'
    +'\xe0FmX\xa5\x97ig*\xa6\n\xd5\x87\xb8H\x1d\xe4\xbb\xa5R\xa1dWyx\x95\x01'
    +'\xecS\xd5@\xb9\x04\x82\x1f2\xb0\xbd\x18U\xb0NHH\xf9\xf8\xcf\xe9\xeb\xd8'
    +'\x91\x1b\xe9W\x81\xa7Y\xd7\xad\x97$\xa7\x10-\xbeWgv\xb7\xc62\xbc9\xb9'
    +'\xb5\xe1\x90W\xe2&U*Y\x94\xc1\xdb\xb3\xb5\xc7\x87\x1a\x11\xf5Sp\x11\x04'
    +'LS',
     '145 byte (2*block size + 1) message'),

    ('b77fb79669ea52c738e58a9ef3ed1501bbe7974478afb5a8bed44549d6232ff8d7aa9'
    +'eeeaf02f6755327951093243110d7bcfc0e51299db793856b57a77e8420',
     '|yS\xd8\x1c\x8d \x8f\xd1\xc9v\x81\xd4\x8fI\xdd\x004V\xde`G[\x84\x07'
    +'\x0e\xf4\x84|3;tW[\x1f\xc8\xd2\xa1\x86\x96D\x85\xa3\xb8cO\xea\xa3YZ'
    +'\xaa\x1a/E\x95\xa7\xd6\xb6\x155c\xde\xe3\x1b\xba\xc4C\xc8\xa3>\xedm]'
    +'\x95j\x98\nh6l%\'\xb5P\xee\x95\x02P\xdf\xb6\x91\xea\xcb\xd5\xd5j\xe1K'
    +'\x97\x06h\xbe\x17L\x89\xdf/\xeaC\xaeR\xf11Bc\x9c\x88O\xd6*6\x83\xc0'
    +'\xc3y/\x0f$\xab\x13\x18\xbc\xb2~!\xf4s\x7f\xabb\xc7~\xa3\x8b\xc8\xfd'
    +'\x1c\xf4\x1f}\xabd\xc1?\xeb\xe7\x15+\xf5\xbbz\xb5\xa7\x8fSF\xd4<\xc7A'
    +'\xcbor\xb7\xb8\x98\x0f&\x8bh\xbfb\xab\xdf\xb1WzRC\x8f\xe1KY\x14\x98'
    +'\xcc\x95\xf0q"\x84`\xc7\xc5\xd5\xce\xb4\xa7\xbd\xe5\x88\xe7\xf2\x1c',
     '214 byte (3*block size - 2) message'),

    ('caca0ff43107f730a7fbe6869fba5af1e626c96303be3bc95155164199c8892219451'
    +'1b24c48911186f647ca246427f2ce7ba747271cd8d7c5e1d127c21f1eaa',
     'zjOO\xdcY\xa1\xd2#8\x1a\xe5\xafI\x8dt\xb7%.\xcfY\xe3\x89\xe4\x910\xc7'
    +'\xea\xeebn{\xd9\x89~\xff\xd9 \x17\xf4\xcc\xdef\xb0D\x04b\xcd\xed\xfd'
    +'5-\x81S\xe6\xa4\xc8\xd7\xa0\x81/p\x1c\xc77\xb5\x17\x8c%V\xf0q\x11 '
    +'\x0e\xb6\'\xdb\xc2\x99\xca\xa7\x92\xdf\xa5\x8f5\x93R\x99\xfa:5\x19'
    +'\xe9\xb01f\xdf\xfa\x15\x91\x03\xff\xa3^\x85w\xf7\xc0\xa8lkF\xfe\x13'
    +'\xdb\x8e,\xdd\x9d\xcf\xba\x85\xbd\xdd\xcc\xe0\xa7\xa8\xe1U\xf8\x1fq-'
    +'\x8e\x9f\xe6F\x15=="\xc8\x11\xbd9\xf80C;"\x13\xddF0\x19A\xb5\x92\x93'
    +'\xfd\n3\xe2\xb6:\xdb\xd9R9\xbc\x011\\F\xfd\xb6x\x87[<\x81\xe0S\xa4'
    +'\x0fX\x1c\xfb\xec$\xa1@K\x16q\xa1\xb8\x8am\x06\x12\x02)Q\x8f\xb1:t'
    +'\xca\n\xc5\xae',
     '215 byte (3*block size - 1) message'),
     
    ('e5106b2a0d49d6d1e13e3323232101cea5da71caa24e70efcac57e0ccf156cdf4c24'
    +'92b03ce0e13437018dab76b9c989883bea69e849f33bb937a397b84ada6a',
     "\xd9\xfa\xa1L\xeb\xe9\xb7\xdeU\x1bl\x07e@\x9a3\x93\x85b\x01;^\x8e\x0e"
    +"\x1e\nd\x18\xdfs\x99\xd0\xa6\xa7q\xfb\x81\xc3\xca\x9b\xd3\xbb\x8e)Q"
    +"\xb0\xbcy%%\xa2\x94\xeb\xd1\x086\x88\x80o\xe5\xe7\xf1\xe1\x7f\xd4\xe3"
    +"\xa4\x1d\x00\xc8\x9e\x8f\xcfJ6<\xae\xdb\x1a\xcbU\x8e=V/\x13\x02\xb3\xd8;"
    +"\xb8\x86\xed'\xb7`3y\x811\xda\xb0[B\x178\x1e\xaa\xa7\xba\x15\xec\x82"
    +"\x0b\xb5\xc1;Qm\xd6@\xea\xecZ'\xd0_\xdf\xca\x0f5\xb3\xa51!F\x80kL\x02u"
    +"\xbc\xd0\xaa\xa3\xb2\x01\x7f4iu\xdbVo\x9bM\x13\x7fN\xe1\x06D\xc2\xa2"
    +"\xdaf\xde\xec\xa54.#d\x95\xc3\xc6(\x05(\xbf\xd3.\x90\xafL\xd9\xbb\x90"
    +"\x8f4\x01+R\xb4\xbcV\xd4\x8c\xc8\xa6\xb5\x9b\xab\x01I\x88\xea\xbd\x12"
    +"\xe1\xa0\xa1\xc2\xe1p\xe7",
     '216 byte (3*block size) message'),
    
    ('faee462e4bced12ad54d3757d644396ed9203037741661aea32bccadae568c4bdc925'
    +'eda76610e964fbe3fb26b33bc0bc123ddf9b528715317ce5c92e00ac96f',
     '-\x84\'C=\x0ca\xf2\xd9l\xfe\x80\xcf\x1e\x93"e\xa1\x916\\;a\xaa\xa3'
    +'\xd6\xdc\xc09\xf6\xba*\xd5*j\x8c\xc3\x0f\xc1\x0fp^kw\x05\x10Yw\xfa'
    +'Il\x1cp\x8a\'z\x12C\x04\xf1\xfc@\x91\x1etA\xd1\xb5\xe7{\x95\x1a\xad'
    +'{\x01\xfd]\xb1\xb3w\xd1e\xb0[\xbf\x89\x80B\xe3\x96`\xca\xf8\xb2y\xfe'
    +'R)\xd1\xa8\xdb\x86\xc0\x99\x9e\xd6^S\xd0\x1c\xcb\xc4\xb41s\xcc\xf9'
    +'\x92\xb3\xa1E\x86\xf6\xbaB\xf5\xfe0\xaf\xa8\xae@\xc5\xdf)\x96o\x93F'
    +'\xda_\x8b5\xf1j\x1d\xe3\xabm\xe0\xf4w\xd8\xd8f\t\x18\x06\x0e\x88\xb9'
    +'\xb9\xe9\xcajB\x07\x03;\x87\xa8\x12\xdb\xf5TM9\xe4\x88 \x10\xf8+l\xe0'
    +'\x05\xf8\xe8\xffo\xe3\xc3\x80k\xc2\xb7<+\x83\xaf\xb7\x044V)0O\x9f'
    +'\x865\x87\x12\xe9\xfa\xe3\xca>',
     '217 byte (3*block size + 1) message'),
    
    ('3d370dc850bc7e159cee3f24d9e915b5b1306ff403c32c7a3a3844f3fc8d90e35'
    +'f56d83bdd9c637bc45e440e1f27ccd56b6b3872ec19101bbe31845108dce929',
     "19\x84\x0b\x8a\xd4\xbc\xd3\x90\x92\x91o\xd9\xd0\x17\x98"
    +"\xffZ\xa1\xe4\x8f4p,r\xdf\xe7K\x12\xe9\x8a\x11N1\x8c\xdd-G"
    +"\xa9\xc3 \xff\xf9\x08\xa8\xdb\xc2\xa5\xb1\xd8rg\xc8\xe9\x83"
    +"\x82\x98a\xa5gU\x8b7\xb2\x92\xd4W^ \r\xe9\xf1\xdeEu_\xaf\xf9"
    +"\xef\xae4\x96NC6\xc2Y\xf1\xe6e\x99\xa7\xc9\x04\xec\x02S\x9f"
    +"\x1a\x8e\xab\x87\x06\xe0\xb4\xf4\x8fr\xfe\xc2yI\t\xeeJ{\t-`a"
    +"\xc7D\x81\xc9\xe2\x1b\x932\xdc|nH-\x7f\x9c\xc3!\x0b8\xa6\xf8"
    +"\x8fy\x18\xc2\xd8\xc5^d\xa4(\xce+h\xfd\x07\xabW*\x8b\n#\x88fO"
    +"\x99H\x9f\x04\xebT\xdf\x13v'\x18\x10\xe0\xe7\xbc\xe3\x96\xf5"
    +"(\x07q\x0e\r\xea\x94\xebI\xf4\xb3g'\x12`\xc3Ek\x98\x18\xfc"
    +"zr#Nk\xf2 _\xf6\xa3eF P\x15\xeb\xd7\xd8\xc2Rz\xa40\xf5\x8e\x0e"
    +"\x8a\xc9z{ky<\xd4\x03\xd5\x17\xd6b\x95\xf3z4\xd0\xb7\xd2\xfa{"
    +"\xc3E\xac\x04\xca\x1e&d\x80\xde\xec9\xf5\xc8\x86A\xc9\xdc\x0b"
    +"\xd15\x81X\xfd\xec\xdd\x96h[\xbb\xb5\xc1\xfe^\xa8\x9d,\xb4\xa9"
    +"\xd5\xd1+\xb8\xc8\x93(\x1f\xf3\x8e\x87\xd6\xb4\x84\x1f\x06P\t"
    +"-D~\x01? \xea\x93N\x18", 
     '319 bytes message'),
     
# Test vectors from http://www.di-mgt.com.au/sha_testvectors.html
    ('18587dc2ea106b9a1563e32b3312421ca164c7f1f07bc922a9c83d77cea3a1e5d'
    +'0c69910739025372dc14ac9642629379540c17e2a65b19d77aa511a9d00bb96',
     'abc',
     '"abc", the bit string (0x)616263 of length 24 bits.'),
     
    ('6aa6d3669597df6d5a007b00d09c20795b5c4218234e1698a944757a488ecdc09'
    +'965435d97ca32c3cfed7201ff30e070cd947f1fc12b9d9214c467d342bcba5d',
     'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq',
     ' "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq" (length 448 bits).'),
     
    ('ac2fb35251825d3aa48468a9948c0a91b8256f6d97d8fa4160faff2dd9dfcc24f'
    +'3f1db7a983dad13d53439ccac0b37e24037e7b95f80f59f37a2f683c4ba4682',
     'abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnh'
     +'ijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu',
     '896 bits message'),
     
    ('5cf53f2e556be5a624425ede23d0e8b2c7814b4ba0e4e09cbbf3c2fac7056f61e'
    +'048fc341262875ebc58a5183fea651447124370c1ebf4d6c89bc9a7731063bb',
     'a' * 1000000,
     'one million (1,000,000) repetitions of the character "a" (0x61).'),

]

def get_tests(config={}):
    from Crypto.Hash import SHA3_512
    from common import make_hash_tests
    return make_hash_tests(SHA3_512, "SHA3_512", test_data,
        digest_size=SHA3_512.digest_size,
        oid="*-not yet assigned-*")

if __name__ == '__main__':
    import unittest
    suite = lambda: unittest.TestSuite(get_tests())
    unittest.main(defaultTest='suite')

# vim:set ts=4 sw=4 sts=4 expandtab:
