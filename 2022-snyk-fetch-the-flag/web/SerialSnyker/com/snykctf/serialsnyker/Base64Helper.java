package com.snykctf.serialsnyker;

import java.io.Serializable;
import java.util.Base64;

public class Base64Helper implements Serializable {
    public String base64;
    private static final long serialVersionUID = 4117174845797624561L;

    public Base64Helper(String base64) {
        this.base64 = base64;
    }

    public String decode() {
        return new String(Base64.getDecoder().decode(this.base64));
    }
}
