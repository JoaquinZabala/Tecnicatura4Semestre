import jwt from "jsonwebtoken";

export const createAccesoToken = (paylod) =>  {
    return new Promise((resolve, reject)=> {
        jwt.sign(paylod,"xyz123",{expiresIn: "1d"},
        (err, yoken)=>{
        if(err) reject(err);
        resolve(token);
    });
    });
};