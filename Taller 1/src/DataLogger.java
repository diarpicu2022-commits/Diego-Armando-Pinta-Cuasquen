//Caso de estudio: Sistema de monitoreo IoT

import java.io.FileWriter; //create .txt
import java.io.IOException; //easy writte text
import java.io.PrintWriter;

public class DataLogger {

    // Instance
    private static volatile DataLogger instance;

    private PrintWriter writer;

    // Constructor
    private DataLogger() {
        try {
            writer = new PrintWriter(new FileWriter("datosSensores.txt", true));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // access
    public static DataLogger getInstance() {
        if (instance == null) {
            synchronized (DataLogger.class) {
                if (instance == null) {
                    instance = new DataLogger();
                }
            }
        }
        return instance;
    }

    //method
    public void log(String mensaje) {
        writer.println(mensaje);
        writer.flush();
    }
}







