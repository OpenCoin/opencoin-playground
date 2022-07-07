```plantuml
hide empty description
actor Alice as alice
actor Bob as bob
rectangle Issuer as issuer

alice <--> issuer: 1. CDDSerial
alice <--> issuer: 2. CDDC
alice <--> issuer: 3. MKC
alice <--> issuer: 4. Minting
alice --> bob: 5. coinstack
bob --> issuer: 6. Renewal
issuer --> bob: 7. Delay
bob --> issuer: 8. Resume
issuer --> bob: 9. Response\nMinting
bob-->issuer: 10. Redeeming


```