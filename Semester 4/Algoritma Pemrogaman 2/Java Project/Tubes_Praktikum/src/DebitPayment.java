
public class DebitPayment extends javax.swing.JFrame {
public Struk struk = new Struk();
    
    public DebitPayment() {
        initComponents();
        this.setLocationRelativeTo(null);
    }
    public DebitPayment(String order,String payment) {
        initComponents();
        this.setLocationRelativeTo(null);
        struk.Order(order); // menyimpan data struk
        struk.Payment(payment); // menyimpan data struk
    }

    
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        bri = new javax.swing.JButton();
        bca = new javax.swing.JButton();
        bni = new javax.swing.JButton();
        mandiri = new javax.swing.JButton();
        back = new javax.swing.JButton();
        BNI = new javax.swing.JLabel();
        LIVIN = new javax.swing.JLabel();
        BCA = new javax.swing.JLabel();
        BRI = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jPanel1.setBackground(new java.awt.Color(255, 255, 255));

        bri.setBackground(new java.awt.Color(204, 51, 0));
        bri.setFont(new java.awt.Font("Rockwell", 1, 18)); // NOI18N
        bri.setForeground(new java.awt.Color(255, 255, 255));
        bri.setText("BRI");
        bri.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                briActionPerformed(evt);
            }
        });

        bca.setBackground(new java.awt.Color(204, 51, 0));
        bca.setFont(new java.awt.Font("Rockwell", 1, 18)); // NOI18N
        bca.setForeground(new java.awt.Color(255, 255, 255));
        bca.setText("BCA");
        bca.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                bcaActionPerformed(evt);
            }
        });

        bni.setBackground(new java.awt.Color(204, 51, 0));
        bni.setFont(new java.awt.Font("Rockwell", 1, 18)); // NOI18N
        bni.setForeground(new java.awt.Color(255, 255, 255));
        bni.setText("BNI");
        bni.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                bniActionPerformed(evt);
            }
        });

        mandiri.setBackground(new java.awt.Color(204, 51, 0));
        mandiri.setFont(new java.awt.Font("Rockwell", 1, 18)); // NOI18N
        mandiri.setForeground(new java.awt.Color(255, 255, 255));
        mandiri.setText("MANDIRI");
        mandiri.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                mandiriActionPerformed(evt);
            }
        });

        back.setBackground(new java.awt.Color(255, 204, 0));
        back.setFont(new java.awt.Font("NSimSun", 1, 14)); // NOI18N
        back.setText("BACK");
        back.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                backActionPerformed(evt);
            }
        });

        BNI.setBackground(new java.awt.Color(241, 89, 35));
        BNI.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Gambar/BNI.png"))); // NOI18N

        LIVIN.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Gambar/Screenshot 2024-06-15 151857.png"))); // NOI18N

        BCA.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Gambar/BCA.png"))); // NOI18N

        BRI.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Gambar/Screenshot 2024-06-15 152916.png"))); // NOI18N

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(93, 93, 93)
                        .addComponent(LIVIN, javax.swing.GroupLayout.PREFERRED_SIZE, 72, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(72, 72, 72)
                        .addComponent(BRI))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(mandiri)
                            .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                .addGroup(jPanel1Layout.createSequentialGroup()
                                    .addGap(61, 61, 61)
                                    .addComponent(bca, javax.swing.GroupLayout.PREFERRED_SIZE, 119, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                                    .addContainerGap()
                                    .addComponent(BCA, javax.swing.GroupLayout.PREFERRED_SIZE, 72, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addGap(18, 18, 18))))
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addGap(37, 37, 37)
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(bni, javax.swing.GroupLayout.PREFERRED_SIZE, 119, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(bri, javax.swing.GroupLayout.PREFERRED_SIZE, 119, javax.swing.GroupLayout.PREFERRED_SIZE)))
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addGap(66, 66, 66)
                                .addComponent(BNI, javax.swing.GroupLayout.PREFERRED_SIZE, 58, javax.swing.GroupLayout.PREFERRED_SIZE)))))
                .addContainerGap(64, Short.MAX_VALUE))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addGap(0, 0, Short.MAX_VALUE)
                .addComponent(back, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(158, 158, 158))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(58, 58, 58)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(LIVIN, javax.swing.GroupLayout.PREFERRED_SIZE, 73, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(BRI))
                .addGap(36, 36, 36)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(mandiri)
                    .addComponent(bri))
                .addGap(38, 38, 38)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(BNI, javax.swing.GroupLayout.PREFERRED_SIZE, 55, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(BCA, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 35, Short.MAX_VALUE)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(bca)
                    .addComponent(bni))
                .addGap(52, 52, 52)
                .addComponent(back)
                .addGap(61, 61, 61))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void backActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_backActionPerformed
        PaymentMethod A = new PaymentMethod(struk.Order.getText());
        A.setVisible(true);
        this.setVisible(false);
    }//GEN-LAST:event_backActionPerformed

    private void mandiriActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_mandiriActionPerformed
    Menu A = new Menu(struk.Order.getText(),struk.Payment.getText()+" - Mandiri"); //untuk bikin objek JFrame setelah di next
    A.setVisible(true); // memunculkan JFrame baru
    this.setVisible(false); // menghapus JFrame sebelumnya
    }//GEN-LAST:event_mandiriActionPerformed

    private void briActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_briActionPerformed
    Menu A = new Menu(struk.Order.getText(),struk.Payment.getText()+" - BRI");
    A.setVisible(true);
    this.setVisible(false);
    }//GEN-LAST:event_briActionPerformed

    private void bcaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_bcaActionPerformed
    Menu A = new Menu(struk.Order.getText(),struk.Payment.getText()+" - BCA");
    A.setVisible(true);
    this.setVisible(false);
    }//GEN-LAST:event_bcaActionPerformed

    private void bniActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_bniActionPerformed
    Menu A = new Menu(struk.Order.getText(),struk.Payment.getText()+" - BNI");
    A.setVisible(true);
    this.setVisible(false);
    }//GEN-LAST:event_bniActionPerformed

    
    public static void main(String args[]) {
        
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new DebitPayment().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel BCA;
    private javax.swing.JLabel BNI;
    private javax.swing.JLabel BRI;
    private javax.swing.JLabel LIVIN;
    private javax.swing.JButton back;
    private javax.swing.JButton bca;
    private javax.swing.JButton bni;
    private javax.swing.JButton bri;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JButton mandiri;
    // End of variables declaration//GEN-END:variables
}
