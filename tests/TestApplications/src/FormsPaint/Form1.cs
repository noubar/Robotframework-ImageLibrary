namespace FormsPaint
{
    public partial class Form1 : Form
    {
        bool down = false;
        Point previousPoint;
        Graphics g;
        Pen pb;
        Pen pw;
        Pen p;
        Bitmap b;
        public Form1()
        {
            InitializeComponent();
            InitializeCanvas();
        }
        private void InitializeCanvas()
        {
            b = new Bitmap(this.Width, this.Height);
            g = Graphics.FromImage(b);
            g.Clear(Color.White);
            panel1.BackgroundImage = b;
            pb = new Pen(Brushes.Black);
            pw = new Pen(Brushes.White);
            p = pb;
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
        }
        private void panel1_MouseMove(object sender, MouseEventArgs e)
        {
            if (down)
            {
                g.DrawLine(p, previousPoint, e.Location);
                previousPoint = e.Location;
                panel1.Invalidate();
            }
        }

        private void panel1_MouseUp(object sender, MouseEventArgs e)
        {
            down = false;
        }

        private void panel1_MouseDown(object sender, MouseEventArgs e)
        {
            down = true;
            if (e.Button == MouseButtons.Left)
                p = pb;
            else if (e.Button == MouseButtons.Right)
                p = pw;
            previousPoint = e.Location;
        }

        private void panel1_MouseClick(object sender, MouseEventArgs e)
        {
            g.DrawEllipse(p, e.X, e.Y, 2, 2);
            panel1.Invalidate();
        }

        private void Form1_SizeChanged(object sender, EventArgs e)
        {
            InitializeCanvas();
        }
    }
}
