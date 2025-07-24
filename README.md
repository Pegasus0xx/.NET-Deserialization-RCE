# .NET-Deserialization-RCE

## Concept

The code decodes a Base64-encoded JSON payload from a cookie named `SessionData` and deserializes it using `JavaScriptSerializer` with `SimpleTypeResolver`.

📄 [`src/vuln.cs`](src/vuln.cs)

```csharp
var serializer = new JavaScriptSerializer(new SimpleTypeResolver());
var resultObject = serializer.Deserialize<object>(jsonPayload);
```

This enables attackers to inject exploitable .NET types (e.g., `System.Diagnostics.Process`) via the `__type` property in JSON, leading to Remote Code Execution (RCE).

https://github.com/user-attachments/assets/57bbb91b-0612-4a38-a0ed-7e6fab1cbdd4

---
> 💬 *"Insecure deserializers are vulnerable when deserializing untrusted data. An attacker could modify the serialized data to include unexpected types to inject objects with malicious side effects."*  
> — Microsoft [CA2321 documentation](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca2321)
