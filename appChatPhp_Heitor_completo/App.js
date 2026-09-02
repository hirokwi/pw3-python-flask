import React, { useState, useEffect, useRef } from "react";
import {
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity,
  FlatList,
  KeyboardAvoidingView,
  Platform,
} from "react-native";
import axios from "axios";

// ATENÇÃO: troque pelo IP da sua máquina na rede (ipconfig / ifconfig)
const API_URL = "http://10.239.23.49/aulaPAMII/chatOdonto";

// Emojis temáticos do consultório odontológico, sorteados por paciente
const EMOJIS_POSSIVEIS = ["😁", "🦷", "🪥", "👩‍⚕️", "🧑‍⚕️", "💙", "📅"];
const EMOJI_PADRAO = "🙂";

export default function App() {
  const [paciente, setPaciente] = useState("");
  const [nomeConfirmado, setNomeConfirmado] = useState(false);
  const [mensagem, setMensagem] = useState("");
  const [mensagens, setMensagens] = useState([]);
  const [emojisPacientes, setEmojisPacientes] = useState({});
  const flatListRef = useRef();

  useEffect(() => {
    if (nomeConfirmado) {
      carregarMensagens();
      marcarComoLido();

      const interval = setInterval(() => {
        carregarMensagens();
        marcarComoLido();
      }, 3000);

      return () => clearInterval(interval);
    }
  }, [nomeConfirmado]);

  const marcarComoLido = async () => {
    try {
      await axios.post(`${API_URL}/marcar_lido.php`, { paciente });
      carregarMensagens();
    } catch (err) {
      console.log("Erro ao marcar como lido", err);
    }
  };

  const carregarMensagens = async () => {
    try {
      const res = await axios.get(`${API_URL}/listar.php`);
      const msgs = res.data.reverse();
      setMensagens(msgs);

      setEmojisPacientes((prev) => {
        const novoMapa = { ...prev };

        msgs.forEach((msg) => {
          if (!novoMapa[msg.paciente]) {
            const emoji =
              EMOJIS_POSSIVEIS[
                Math.floor(Math.random() * EMOJIS_POSSIVEIS.length)
              ];

            novoMapa[msg.paciente] = emoji;
          }
        });

        return novoMapa;
      });
    } catch (err) {
      console.log("Erro ao buscar mensagens", err);
    }
  };

  const enviarMensagem = async () => {
    if (mensagem.trim() === "") return;

    try {
      await axios.post(`${API_URL}/enviar.php`, {
        paciente,
        mensagem,
      });

      setMensagem("");
      carregarMensagens();
    } catch (err) {
      console.log("Erro ao enviar mensagem", err);
    }
  };

  const formatarHora = (dataHora) => {
    if (!dataHora) return "";

    const date = new Date(dataHora);

    return date.toLocaleTimeString("pt-BR", {
      hour: "2-digit",
      minute: "2-digit",
    });
  };

  const renderStatus = (status) => {
    if (status === "entregue") return "✅✅";
    if (status === "lido") return "✅👌";
    return "";
  };

  // Tela Inicial - Recepção do Consultório
  if (!nomeConfirmado) {
    return (
      <View style={styles.loginContainer}>
        <Text style={styles.iconeTopo}>🦷</Text>
        <Text style={styles.titulo}>Consultório Odontológico</Text>
        <Text style={styles.tituloDestaque}>Sorriso Feliz</Text>

        <Text style={styles.subtitulo}>
          Digite seu nome para falar com a recepção
        </Text>

        <TextInput
          style={styles.input}
          placeholder="Nome do paciente"
          placeholderTextColor="#7a93a8"
          value={paciente}
          onChangeText={setPaciente}
        />

        <TouchableOpacity
          style={styles.botaoEntrar}
          onPress={() => paciente.trim() !== "" && setNomeConfirmado(true)}
        >
          <Text style={styles.botaoTexto}>Entrar no Chat 🦷</Text>
        </TouchableOpacity>
      </View>
    );
  }

  // Tela do Chat com a Recepção
  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === "ios" ? "padding" : undefined}
    >
      <Text style={styles.header}>🦷 Sorriso Feliz - Olá, {paciente}</Text>

      <FlatList
        ref={flatListRef}
        data={mensagens}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => {
          const isMe = item.paciente === paciente;

          return (
            <View
              style={[styles.msg, isMe ? styles.msgMinha : styles.msgOutro]}
            >
              {!isMe && (
                <Text style={styles.usuario}>
                  {emojisPacientes[item.paciente] || EMOJI_PADRAO}{" "}
                  {item.paciente}
                </Text>
              )}

              <Text style={styles.texto}>{item.mensagem}</Text>

              <View style={styles.linhaHora}>
                <Text style={styles.hora}>{formatarHora(item.data_hora)}</Text>

                {isMe && (
                  <Text
                    style={[
                      styles.status,
                      item.status === "lido" && styles.statusLido,
                    ]}
                  >
                    {renderStatus(item.status)}
                  </Text>
                )}
              </View>
            </View>
          );
        }}
        onContentSizeChange={() =>
          flatListRef.current.scrollToEnd({
            animated: true,
          })
        }
        onLayout={() =>
          flatListRef.current.scrollToEnd({
            animated: true,
          })
        }
      />

      <View style={styles.inputArea}>
        <TextInput
          style={styles.inputMensagem}
          placeholder="Digite sua mensagem para a recepção..."
          placeholderTextColor="#7a93a8"
          value={mensagem}
          onChangeText={setMensagem}
        />

        <TouchableOpacity style={styles.botaoEnviar} onPress={enviarMensagem}>
          <Text style={styles.botaoTexto}>➤</Text>
        </TouchableOpacity>
      </View>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  loginContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#eaf6f6",
    padding: 20,
  },

  iconeTopo: {
    fontSize: 60,
    marginBottom: 10,
  },

  titulo: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#0f6d6a",
    textAlign: "center",
  },

  tituloDestaque: {
    fontSize: 26,
    fontWeight: "bold",
    marginBottom: 15,
    color: "#12a39c",
  },

  subtitulo: {
    fontSize: 15,
    marginBottom: 20,
    color: "#3a5a5a",
    fontWeight: "600",
    textAlign: "center",
  },

  botaoEntrar: {
    backgroundColor: "#12a39c",
    paddingVertical: 12,
    paddingHorizontal: 30,
    borderRadius: 25,
    marginTop: 15,
  },

  botaoTexto: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "bold",
  },

  container: {
    flex: 1,
    backgroundColor: "#eaf6f6",
    padding: 10,
    paddingTop: 40,
  },

  header: {
    fontSize: 19,
    fontWeight: "bold",
    textAlign: "center",
    marginBottom: 10,
    color: "#0f6d6a",
  },

  msg: {
    maxWidth: "75%",
    marginVertical: 5,
    padding: 10,
    borderRadius: 15,
  },

  msgMinha: {
    backgroundColor: "#12a39c",
    alignSelf: "flex-end",
    borderBottomRightRadius: 0,
  },

  msgOutro: {
    backgroundColor: "#fff",
    alignSelf: "flex-start",
    borderBottomLeftRadius: 0,
  },

  usuario: {
    fontWeight: "bold",
    marginBottom: 3,
    color: "#0f6d6a",
  },

  texto: {
    color: "#000",
    fontSize: 15,
  },

  linhaHora: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "flex-end",
    marginTop: 3,
  },

  hora: {
    fontSize: 11,
    color: "#666",
    marginRight: 5,
  },

  status: {
    fontSize: 12,
    color: "#666",
  },

  statusLido: {
    color: "#1e90ff",
  },

  inputArea: {
    flexDirection: "row",
    alignItems: "center",
    backgroundColor: "#fff",
    borderRadius: 30,
    paddingHorizontal: 10,
    paddingVertical: 5,
    margin: 10,
    elevation: 3,
  },

  inputMensagem: {
    flex: 1,
    paddingHorizontal: 15,
    fontSize: 16,
  },

  botaoEnviar: {
    backgroundColor: "#12a39c",
    width: 45,
    height: 45,
    borderRadius: 25,
    justifyContent: "center",
    alignItems: "center",
  },

  input: {
    width: 240,
    borderColor: "#12a39c",
    borderRadius: 10,
    borderWidth: 2,
    backgroundColor: "#fff",
    paddingHorizontal: 12,
    paddingVertical: 10,
    marginBottom: 5,
  },
});
