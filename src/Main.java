import javax.swing.*;
import java.sql.*;

public class Main {

    private static JFrame frame; // We make this here so can use this for other methods

    /**
     * This is the method that holds the code to handle the Log in screen. I still need to add on the database
     * connection, which I'll do when I have a better idea of how I will do this.
     */
    private static void home(){
        frame.removeAll(); // resets everything so we can work with it from scratch

        JTextArea topLabel = new JTextArea("Library Management System");
        JButton logInButton = new JButton("Login/\nCreate Account");
        JButton checkInButton = new JButton("Check In");
        JButton checkOutButton = new JButton("Check Out");
        JButton checkBookStatus = new JButton("Check Books\nChecked out");
        JButton checkAccount = new JButton("Check Account");
        JButton quitApp = new JButton("Quit App");
        JTextArea curDateTime = new JTextArea();


    }
    public static void main(String[] args) {

    }
}
