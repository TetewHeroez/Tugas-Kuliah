package Week7.Praktikum4;

import javax.swing.*;

import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class GUI{
    
    private JPanel input;
    private JPanel output;
    private JPanel exception;
    private static JTextField digit;
    private JButton add;
    private static JTextArea display1;
    private static JTextArea display2;

    public GUI(){
        JFrame form = new JFrame("Deret Fibbonacci");
        form.setSize(400,400);
        form.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        form.setLocationRelativeTo(null);
        form.setLayout(null);



        input = new JPanel(new GridBagLayout());
        input.setBounds(10,10,360,80);
        input.setBorder(BorderFactory.createTitledBorder("input"));
        form.add(input);

        digit = new JTextField(6);
        digit.setPreferredSize(new Dimension(0, 30));
        digit.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
                String numstr = digit.getText();
                char c = e.getKeyChar();
                if (!Character.isDigit(c)) {
                    e.consume();
                }
                else if (numstr.length()>=6) {
                    e.consume();
                }
            }

            @Override
            public void keyPressed(KeyEvent e) {
                
            }

            @Override
            public void keyReleased(KeyEvent e) {
                
            }
        });
        input.add(digit);

        add = new JButton("Add");
        add.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                display1.setText("");
                display2.setText("digit sama: ");
                boolean ketemu = false;
                int index=0;
                int add = Integer.valueOf(digit.getText());
                ArrayList<Integer> barisan = MethodFIbbonacci.Fibbonacci(add);
                for (int i = 0; i < barisan.size(); i++) {
                    display1.append(String.valueOf(barisan.get(i))+" ");
                    if (display1.getText().length()==54) {
                        display1.append("\n");
                    }
                    if (display1.getText().length()==100) {
                        display1.append("\n");
                    }
                    if (MethodFIbbonacci.SameNum(barisan.get(i))) {
                        display2.append(String.valueOf(barisan.get(i))+" ");
                        if (display2.getText().length()==49) {
                            display2.append("\n");
                        }
                    }
                    if (add==barisan.get(i)) {
                        ketemu = true;
                        index = i;
                    }
                }
                display2.append("\n");
                if (ketemu) {
                    display2.append("\nAngka "+digit.getText()+" ditemukan pada suku ke-"+index);
                }
                else{
                    display2.append("\nAngka "+digit.getText()+" tidak berada di barisan Fibbonacci");
                }
            }
        });
        input.add(add);

        output = new JPanel(new GridBagLayout());
        output.setBounds(10,100,360,110);
        output.setBorder(BorderFactory.createTitledBorder("output"));
        form.add(output);

        display1 = new JTextArea();
        display1.setPreferredSize(new Dimension(320, 60));
        display1.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
                e.consume();
            }

            @Override
            public void keyPressed(KeyEvent e) {
                
            }

            @Override
            public void keyReleased(KeyEvent e) {
                
            }
        });
        output.add(display1);

        exception = new JPanel(new GridBagLayout());
        exception.setBounds(10,220,360,120);
        exception.setBorder(BorderFactory.createTitledBorder("exception"));
        form.add(exception);

        display2 = new JTextArea();
        display2.setPreferredSize(new Dimension(320, 80));
        display2.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
                e.consume();
            }

            @Override
            public void keyPressed(KeyEvent e) {
                
            }

            @Override
            public void keyReleased(KeyEvent e) {
                
            }
        });
        exception.add(display2);

        form.setVisible(true);
    }
    public static void main(String[] args) {
        new GUI();
    }
}
