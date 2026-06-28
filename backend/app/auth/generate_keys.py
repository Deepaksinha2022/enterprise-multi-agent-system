from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# RSA allows to generate public and private keys
# serialisation serialization converts Python key objects into 
# a storable format (PEM).
# In RS256, every signature is created using the private key.
# No private key ⇒ cannot sign JWTs.

# # Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Public_exponent - industry standard value for RSA
# used during RSA key generation
# Specifies the RSA key length in bits. - key_size
# larger key size more difficult to break it

# Generate public key
public_key = private_key.public_key()

# public key is generated from private key
# always generated in a pair - mathematical relation 
# between them is fixed - 

# private key - signs the JWT 
#             - only authentication server should have it
# Public keys - verifies the signature
#             - can be shared with other services

# with open("private.pem", "wb") creates a PEM file in binary 
# write mode. It is used to persist the generated private RSA
# key to disk so it can be reused after the application restarts

# Save private key
# why save  - the keys only exist in RAM
# we save it to disk for storage

with open("private.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

# PEM is the universal standard understood 
# by JWT, HTTPS, SSL/TLS, etc.
# public key is not encrypted as it is meant to be shared
# for verification

# Save public key
with open("public.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

print("RSA keys generated successfully.")