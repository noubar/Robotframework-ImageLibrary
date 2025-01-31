using System.Linq;
using System.Windows;

namespace WpfApplication
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App
    {
        void App_Startup(object sender, StartupEventArgs e)
        {
            string tabArg = e.Args.FirstOrDefault() ?? "0"; // Default to first tab (index 0)
            if (!int.TryParse(tabArg, out int tabIndex))
            {
                tabIndex = 0; // Fallback if invalid argument
            }

            MainWindow mainWindow = new MainWindow(tabIndex);
            mainWindow.Show();
        }
    }
}
