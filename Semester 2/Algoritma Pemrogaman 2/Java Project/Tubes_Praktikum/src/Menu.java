
import java.util.ArrayList;


public class Menu extends javax.swing.JFrame {
public Struk struk = new Struk();

    
    public Menu() {
        initComponents();
        this.setLocationRelativeTo(null);
    }
    public Menu(String order,String payment) {
        initComponents();
        this.setLocationRelativeTo(null);
        struk.Order(order);
        struk.Payment(payment);
    }

    
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jSpinner1 = new javax.swing.JSpinner();
        jPanel1 = new javax.swing.JPanel();
        makanan = new javax.swing.JLabel();
        mealbox = new javax.swing.JLabel();
        chicken = new javax.swing.JLabel();
        chebyshev = new javax.swing.JLabel();
        roti = new javax.swing.JLabel();
        donat = new javax.swing.JLabel();
        pisang = new javax.swing.JLabel();
        backaction = new javax.swing.JButton();
        jmlchebyshev = new javax.swing.JSpinner();
        jmlfpk = new javax.swing.JSpinner();
        jmlmaclaurin = new javax.swing.JSpinner();
        jmllegendre = new javax.swing.JSpinner();
        jmlfourier = new javax.swing.JSpinner();
        jmlkpb = new javax.swing.JSpinner();
        jmllaplace = new javax.swing.JSpinner();
        next = new javax.swing.JButton();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        jmlaljabar = new javax.swing.JSpinner();
        jmlanalisis = new javax.swing.JSpinner();
        jmlkalkulus = new javax.swing.JSpinner();
        jmlmatdis = new javax.swing.JSpinner();
        jmlmatrix = new javax.swing.JSpinner();
        jmlinvers = new javax.swing.JSpinner();
        jmltakhingga = new javax.swing.JSpinner();
        fpk = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jPanel1.setBackground(new java.awt.Color(204, 51, 0));
        jPanel1.setForeground(new java.awt.Color(255, 255, 255));

        makanan.setFont(new java.awt.Font("NSimSun", 1, 24)); // NOI18N
        makanan.setForeground(new java.awt.Color(255, 204, 0));
        makanan.setText("- MENU -");

        mealbox.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        mealbox.setForeground(new java.awt.Color(255, 255, 255));
        mealbox.setText("Mealbox KPB                    12.000");

        chicken.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        chicken.setForeground(new java.awt.Color(255, 255, 255));
        chicken.setText("Chicken Maclaurin           20.000");

        chebyshev.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        chebyshev.setForeground(new java.awt.Color(255, 255, 255));
        chebyshev.setText("Chebyshev Burger           17.000");

        roti.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        roti.setForeground(new java.awt.Color(255, 255, 255));
        roti.setText("Roti Bakar Legendre        10.000");

        donat.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        donat.setForeground(new java.awt.Color(255, 255, 255));
        donat.setText("Donat Fourier                    5.000");

        pisang.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        pisang.setForeground(new java.awt.Color(255, 255, 255));
        pisang.setText("Pisang Goreng Laplace    10.000");

        backaction.setBackground(new java.awt.Color(255, 204, 0));
        backaction.setFont(new java.awt.Font("NSimSun", 1, 14)); // NOI18N
        backaction.setText("BACK");
        backaction.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                backactionActionPerformed(evt);
            }
        });

        jmlchebyshev.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N

        jmlfpk.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N

        jmlmaclaurin.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N

        jmllegendre.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N

        jmlfourier.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N

        jmlkpb.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N

        jmllaplace.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N

        next.setBackground(new java.awt.Color(255, 204, 0));
        next.setFont(new java.awt.Font("NSimSun", 1, 14)); // NOI18N
        next.setText("NEXT");
        next.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                nextActionPerformed(evt);
            }
        });

        jLabel2.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        jLabel2.setForeground(new java.awt.Color(255, 255, 255));
        jLabel2.setText("Aljabar Latte                    15.000");

        jLabel3.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        jLabel3.setForeground(new java.awt.Color(255, 255, 255));
        jLabel3.setText("Analisis Machiato            24.000");

        jLabel4.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        jLabel4.setForeground(new java.awt.Color(255, 255, 255));
        jLabel4.setText("Kalkulus Gula Aren          19.000");

        jLabel5.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        jLabel5.setForeground(new java.awt.Color(255, 255, 255));
        jLabel5.setText("Matdis Frappe                  20.000");

        jLabel6.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        jLabel6.setForeground(new java.awt.Color(255, 255, 255));
        jLabel6.setText("Matrix Milkshake             12.000");

        jLabel7.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        jLabel7.setForeground(new java.awt.Color(255, 255, 255));
        jLabel7.setText("Es Teh Invers                    10.000");

        jLabel8.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        jLabel8.setForeground(new java.awt.Color(255, 255, 255));
        jLabel8.setText("Mineral Tak Hingga           5.000");

        jmlaljabar.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        jmlaljabar.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyTyped(java.awt.event.KeyEvent evt) {
                jmlaljabarKeyTyped(evt);
            }
        });

        jmlanalisis.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N

        jmlkalkulus.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N

        jmlmatdis.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N

        jmlmatrix.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N

        jmlinvers.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N

        jmltakhingga.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N

        fpk.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        fpk.setForeground(new java.awt.Color(255, 255, 255));
        fpk.setText("FPK Fried Rice                  15.000");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addContainerGap(52, Short.MAX_VALUE)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                        .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                            .addComponent(donat, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED))
                        .addGroup(jPanel1Layout.createSequentialGroup()
                            .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                .addComponent(jLabel6, javax.swing.GroupLayout.PREFERRED_SIZE, 199, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                                    .addComponent(jLabel5, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                    .addComponent(jLabel4, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                    .addComponent(jLabel3, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                    .addComponent(jLabel2, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                    .addComponent(pisang, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 200, Short.MAX_VALUE)))
                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED))
                        .addComponent(makanan, javax.swing.GroupLayout.Alignment.TRAILING)
                        .addComponent(mealbox, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(fpk, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(chebyshev, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(chicken, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(roti, javax.swing.GroupLayout.DEFAULT_SIZE, 200, Short.MAX_VALUE)
                        .addComponent(jLabel8, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(jLabel7, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addComponent(backaction, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(131, 131, 131)))
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jmlchebyshev, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jmllegendre, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jmlfourier, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jmlkpb, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jmllaplace, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jmlaljabar, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jmlanalisis, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jmlkalkulus, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jmlmatdis, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jmlmatrix, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jmlinvers, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jmlfpk, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jmlmaclaurin, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jmltakhingga, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(next, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(67, 67, 67))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(20, 20, 20)
                .addComponent(makanan)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(mealbox)
                    .addComponent(jmlkpb, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jmlfpk, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(fpk))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jmlmaclaurin, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(chicken))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jmlchebyshev, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(chebyshev))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jmllegendre, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(roti))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jmlfourier, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(donat))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jmllaplace, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(pisang))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jmlaljabar, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel2))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jmlanalisis, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel3))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jmlkalkulus, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel4))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jmlmatdis, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel5))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jmlmatrix, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel6))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jmlinvers, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel7))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jmltakhingga, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel8))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(next)
                    .addComponent(backaction))
                .addContainerGap(20, Short.MAX_VALUE))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jmlaljabarKeyTyped(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_jmlaljabarKeyTyped

    }//GEN-LAST:event_jmlaljabarKeyTyped

    private void nextActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_nextActionPerformed
        ArrayList<ArrayList<String>> pesanan = pesanan();
        Struk A = new Struk(struk.Order.getText(),struk.Payment.getText(),pesanan);
        A.setVisible(true);
        this.setVisible(false);
    }//GEN-LAST:event_nextActionPerformed

    private void backactionActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_backactionActionPerformed
        PaymentMethod A = new PaymentMethod(struk.Order.getText());
        A.setVisible(true);
        this.setVisible(false);
    }//GEN-LAST:event_backactionActionPerformed

    public ArrayList<ArrayList<String>> pesanan(){
       ArrayList<ArrayList<String>> pesan = new ArrayList();
       if(!jmlkpb.getValue().toString().equals("0")){
           ArrayList p = new ArrayList();
           p.add("Mealbox KPB");
           p.add("12.000");
           p.add(jmlkpb.getValue());
           p.add((int)jmlkpb.getValue()*12000/1000 +".000");
           pesan.add(p);
       }
       if(!jmlfpk.getValue().toString().equals("0")){
           ArrayList p = new ArrayList();
           p.add("FPK Fried Rice");
           p.add("15.000");
           p.add(jmlfpk.getValue());
           p.add((int)jmlfpk.getValue()*15000/1000 +".000");
           pesan.add(p);
       }
       if(!jmlmaclaurin.getValue().toString().equals("0")){
           ArrayList p = new ArrayList();
           p.add("Chicken Maclaurin");
           p.add("20.000");
           p.add(jmlmaclaurin.getValue());
           p.add((int)jmlmaclaurin.getValue()*20000/1000 +".000");
           pesan.add(p);
       }
       if(!jmlchebyshev.getValue().toString().equals("0")){
           ArrayList p = new ArrayList();
           p.add("Chebyshev Burger");
           p.add("17.000");
           p.add(jmlchebyshev.getValue());
           p.add((int)jmlchebyshev.getValue()*17000/1000 +".000");
           pesan.add(p);
       }
       if(!jmllegendre.getValue().toString().equals("0")){
           ArrayList p = new ArrayList();
           p.add("Roti Bakar Legendre");
           p.add("10.000");
           p.add(jmllegendre.getValue());
           p.add((int)jmllegendre.getValue()*10000/1000 +".000");
           pesan.add(p);
       }
       if(!jmlfourier.getValue().toString().equals("0")){
           ArrayList p = new ArrayList();
           p.add("Donat Fourier");
           p.add("5.000");
           p.add(jmlfourier.getValue());
           p.add((int)jmlfourier.getValue()*5000/1000 +".000");
           pesan.add(p);
       }
       if(!jmllaplace.getValue().toString().equals("0")){
           ArrayList p = new ArrayList();
           p.add("Pisang Goreng Laplace");
           p.add("10.000");
           p.add(jmllaplace.getValue());
           p.add((int)jmllaplace.getValue()*10000/1000 +".000");
           pesan.add(p);
       }
       if(!jmlaljabar.getValue().toString().equals("0")){
           ArrayList p = new ArrayList();
           p.add("Aljabar Latte");
           p.add("15.000");
           p.add(jmlaljabar.getValue());
           p.add((int)jmlaljabar.getValue()*15000/1000 +".000");
           pesan.add(p);
       }
       if(!jmlanalisis.getValue().toString().equals("0")){
           ArrayList p = new ArrayList();
           p.add("Analisis Machiato");
           p.add("24.000");
           p.add(jmlanalisis.getValue());
           p.add((int)jmlanalisis.getValue()*24000/1000 +".000");
           pesan.add(p);
       }
       if(!jmlkalkulus.getValue().toString().equals("0")){
           ArrayList p = new ArrayList();
           p.add("Kalkulus Gula Aren");
           p.add("19.000");
           p.add(jmlkalkulus.getValue());
           p.add((int)jmlkalkulus.getValue()*19000/1000 +".000");
           pesan.add(p);
       }
       if(!jmlmatdis.getValue().toString().equals("0")){
           ArrayList p = new ArrayList();
           p.add("Matdis Frappe");
           p.add("20.000");
           p.add(jmlmatdis.getValue());
           p.add((int)jmlmatdis.getValue()*20000/1000 +".000");
           pesan.add(p);
       }
       if(!jmlmatrix.getValue().toString().equals("0")){
           ArrayList p = new ArrayList();
           p.add("Matrix Milkshake");
           p.add("12.000");
           p.add(jmlmatrix.getValue());
           p.add((int)jmlmatrix.getValue()*12000/1000 +".000");
           pesan.add(p);
       }
       if(!jmlinvers.getValue().toString().equals("0")){
           ArrayList p = new ArrayList();
           p.add("Es Teh Invers");
           p.add("10.000");
           p.add(jmlinvers.getValue());
           p.add((int)jmlinvers.getValue()*10000/1000 +".000");
           pesan.add(p);
       }
       if(!jmltakhingga.getValue().toString().equals("0")){
           ArrayList p = new ArrayList();
           p.add("Mineral Tak Hingga");
           p.add("5.000");
           p.add(jmltakhingga.getValue());
           p.add((int)jmltakhingga.getValue()*5000/1000 +".000");
           pesan.add(p);
       }
       return pesan;
    }
    
    public static void main(String args[]) {
        
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Menu().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton backaction;
    private javax.swing.JLabel chebyshev;
    private javax.swing.JLabel chicken;
    private javax.swing.JLabel donat;
    private javax.swing.JLabel fpk;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JSpinner jSpinner1;
    private javax.swing.JSpinner jmlaljabar;
    private javax.swing.JSpinner jmlanalisis;
    private javax.swing.JSpinner jmlchebyshev;
    private javax.swing.JSpinner jmlfourier;
    private javax.swing.JSpinner jmlfpk;
    private javax.swing.JSpinner jmlinvers;
    private javax.swing.JSpinner jmlkalkulus;
    private javax.swing.JSpinner jmlkpb;
    private javax.swing.JSpinner jmllaplace;
    private javax.swing.JSpinner jmllegendre;
    private javax.swing.JSpinner jmlmaclaurin;
    private javax.swing.JSpinner jmlmatdis;
    private javax.swing.JSpinner jmlmatrix;
    private javax.swing.JSpinner jmltakhingga;
    private javax.swing.JLabel makanan;
    private javax.swing.JLabel mealbox;
    private javax.swing.JButton next;
    private javax.swing.JLabel pisang;
    private javax.swing.JLabel roti;
    // End of variables declaration//GEN-END:variables
}
