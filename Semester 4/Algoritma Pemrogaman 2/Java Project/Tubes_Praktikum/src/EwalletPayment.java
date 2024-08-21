
public class EwalletPayment extends javax.swing.JFrame {
public Struk struk = new Struk();
    
    public EwalletPayment() {
        initComponents();
        this.setLocationRelativeTo(null);
    }
    public EwalletPayment(String order,String payment) {
        initComponents();
        this.setLocationRelativeTo(null);
        struk.Order(order);
        struk.Payment(payment);
    }
    
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel1 = new javax.swing.JLabel();
        jPanel1 = new javax.swing.JPanel();
        shopeepay = new javax.swing.JButton();
        gopay = new javax.swing.JButton();
        ovo = new javax.swing.JButton();
        dana = new javax.swing.JButton();
        back = new javax.swing.JButton();
        SHOPEEPAY = new javax.swing.JLabel();
        GOPAY = new javax.swing.JLabel();
        DANA = new javax.swing.JLabel();
        DANA1 = new javax.swing.JLabel();

        jLabel1.setText("jLabel1");

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jPanel1.setBackground(new java.awt.Color(255, 255, 255));
        jPanel1.setPreferredSize(new java.awt.Dimension(400, 500));

        shopeepay.setBackground(new java.awt.Color(255, 204, 0));
        shopeepay.setFont(new java.awt.Font("Rockwell", 1, 18)); // NOI18N
        shopeepay.setText("SHOPEE PAY");
        shopeepay.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                shopeepayActionPerformed(evt);
            }
        });

        gopay.setBackground(new java.awt.Color(255, 204, 0));
        gopay.setFont(new java.awt.Font("Rockwell", 1, 18)); // NOI18N
        gopay.setText("GOPAY");
        gopay.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                gopayActionPerformed(evt);
            }
        });

        ovo.setBackground(new java.awt.Color(255, 204, 0));
        ovo.setFont(new java.awt.Font("Rockwell", 1, 18)); // NOI18N
        ovo.setText("OVO");
        ovo.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ovoActionPerformed(evt);
            }
        });

        dana.setBackground(new java.awt.Color(255, 204, 0));
        dana.setFont(new java.awt.Font("Rockwell", 1, 18)); // NOI18N
        dana.setText("DANA");
        dana.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                danaActionPerformed(evt);
            }
        });

        back.setBackground(new java.awt.Color(204, 51, 0));
        back.setFont(new java.awt.Font("NSimSun", 1, 14)); // NOI18N
        back.setText("BACK");
        back.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                backActionPerformed(evt);
            }
        });

        SHOPEEPAY.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Gambar/S LOGO.png"))); // NOI18N
        SHOPEEPAY.setText("jLabel2");

        GOPAY.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Gambar/G LOGO FIX.png"))); // NOI18N
        GOPAY.setText("jLabel2");

        DANA.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Gambar/D LOGO.png"))); // NOI18N
        DANA.setText("jLabel2");

        DANA1.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Gambar/O LOGO.png"))); // NOI18N
        DANA1.setText("jLabel2");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(162, 162, 162)
                        .addComponent(back, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(41, 41, 41)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addComponent(gopay, javax.swing.GroupLayout.PREFERRED_SIZE, 146, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(18, 18, 18)
                                .addComponent(shopeepay))
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addComponent(ovo, javax.swing.GroupLayout.PREFERRED_SIZE, 146, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(18, 18, 18)
                                .addComponent(dana, javax.swing.GroupLayout.PREFERRED_SIZE, 146, javax.swing.GroupLayout.PREFERRED_SIZE)))))
                .addContainerGap(49, Short.MAX_VALUE))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addGap(83, 83, 83)
                .addComponent(GOPAY, javax.swing.GroupLayout.PREFERRED_SIZE, 65, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(SHOPEEPAY, javax.swing.GroupLayout.PREFERRED_SIZE, 65, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(87, 87, 87))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addGap(82, 82, 82)
                .addComponent(DANA1, javax.swing.GroupLayout.PREFERRED_SIZE, 65, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(DANA, javax.swing.GroupLayout.PREFERRED_SIZE, 65, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(88, 88, 88))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(77, 77, 77)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(SHOPEEPAY)
                    .addComponent(GOPAY))
                .addGap(18, 18, 18)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(shopeepay)
                    .addComponent(gopay))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 49, Short.MAX_VALUE)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(DANA)
                    .addComponent(DANA1))
                .addGap(18, 18, 18)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(ovo, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(dana))
                .addGap(65, 65, 65)
                .addComponent(back)
                .addGap(66, 66, 66))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, 396, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void backActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_backActionPerformed
        PaymentMethod A = new PaymentMethod(struk.Order.getText());
        A.setVisible(true);
        this.setVisible(false);
    }//GEN-LAST:event_backActionPerformed

    private void shopeepayActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_shopeepayActionPerformed
    Menu A = new Menu(struk.Order.getText(),struk.Payment.getText()+" - SHOPEEPAY");
    A.setVisible(true);
    this.setVisible(false);
    }//GEN-LAST:event_shopeepayActionPerformed

    private void gopayActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_gopayActionPerformed
    Menu A = new Menu(struk.Order.getText(),struk.Payment.getText()+" - GOPAY");
    A.setVisible(true);
    this.setVisible(false);
    }//GEN-LAST:event_gopayActionPerformed

    private void ovoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ovoActionPerformed
    Menu A = new Menu(struk.Order.getText(),struk.Payment.getText()+" - OVO");
    A.setVisible(true);
    this.setVisible(false);
    }//GEN-LAST:event_ovoActionPerformed

    private void danaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_danaActionPerformed
    Menu A = new Menu(struk.Order.getText(),struk.Payment.getText()+" - DANA");
    A.setVisible(true);
    this.setVisible(false);
    }//GEN-LAST:event_danaActionPerformed

    
    public static void main(String args[]) {
        
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new EwalletPayment().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel DANA;
    private javax.swing.JLabel DANA1;
    private javax.swing.JLabel GOPAY;
    private javax.swing.JLabel SHOPEEPAY;
    private javax.swing.JButton back;
    private javax.swing.JButton dana;
    private javax.swing.JButton gopay;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JButton ovo;
    private javax.swing.JButton shopeepay;
    // End of variables declaration//GEN-END:variables
}
