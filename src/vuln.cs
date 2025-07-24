    public class vuln : Controller
    {
        public ActionResult Index()
        {
            var cookieValue = Request.Cookies["SessionData"]?.Value;

            if (string.IsNullOrEmpty(cookieValue))
            {
                ViewBag.Message = "SessionData cookie is missing.";
                return View();
            }

            try
            {

                var decodedBytes = Convert.FromBase64String(cookieValue);
                var jsonPayload = Encoding.UTF8.GetString(decodedBytes);

                var serializer = new JavaScriptSerializer(new SimpleTypeResolver());
                var resultObject = serializer.Deserialize<object>(jsonPayload);

                System.Diagnostics.Debug.WriteLine($"[*] Deserialized: {resultObject}");
                ViewBag.Message = "Deserialization succeeded.";
            }
            catch (Exception ex)
            {
                ViewBag.Message = $"Error: {ex.Message}";
            }

            return View();
        }
    }
