from typing import Dict, List, Any

class KnowledgeBaseTool:
    """Tool for searching knowledge base and retrieving solutions"""
    
    def __init__(self):
        # Simulación de base de conocimientos más completa
        self.knowledge_base = {
            "facturación": {
                "common_issues": [
                    "Cargo duplicado en tarjeta",
                    "Factura no recibida",
                    "Error en monto facturado",
                    "Cambio de método de pago",
                    "Reembolso solicitado"
                ],
                "solutions": {
                    "cargo_duplicado": {
                        "title": "Resolución de Cargo Duplicado",
                        "steps": [
                            "1. Verificar todas las transacciones en el sistema de facturación",
                            "2. Confirmar fechas y montos con el cliente",
                            "3. Identificar si es cargo legítimo o duplicado real",
                            "4. Si es duplicado: procesar reembolso inmediato",
                            "5. Actualizar información de facturación del cliente",
                            "6. Configurar alertas para prevenir futuros duplicados"
                        ],
                        "escalation_needed": False,
                        "estimated_time": "10-15 minutos",
                        "follow_up_required": True
                    },
                    "factura_no_recibida": {
                        "title": "Factura No Recibida",
                        "steps": [
                            "1. Verificar dirección de email registrada en el sistema",
                            "2. Revisar carpeta de spam del cliente",
                            "3. Reenviar factura al email correcto inmediatamente",
                            "4. Configurar notificaciones automáticas",
                            "5. Ofrecer acceso al portal de facturas online",
                            "6. Programar envío de facturas futuras"
                        ],
                        "escalation_needed": False,
                        "estimated_time": "5-10 minutos",
                        "follow_up_required": False
                    }
                }
            },
            "técnico": {
                "common_issues": [
                    "Servicio no funciona",
                    "Conectividad intermitente", 
                    "Error de autenticación",
                    "Rendimiento lento",
                    "Configuración incorrecta"
                ],
                "solutions": {
                    "servicio_no_funciona": {
                        "title": "Servicio No Funciona",
                        "steps": [
                            "1. Verificar estado general del servicio en la región del cliente",
                            "2. Solicitar al cliente que reinicie su conexión/dispositivo",
                            "3. Verificar configuración específica del cliente",
                            "4. Ejecutar diagnósticos remotos del servicio",
                            "5. Si persiste: escalar a soporte técnico nivel 2",
                            "6. Proporcionar número de ticket para seguimiento"
                        ],
                        "escalation_needed": True,
                        "estimated_time": "15-30 minutos",
                        "follow_up_required": True
                    },
                    "conectividad_intermitente": {
                        "title": "Problemas de Conectividad Intermitente",
                        "steps": [
                            "1. Ejecutar diagnóstico completo de red del cliente",
                            "2. Verificar calidad y estabilidad de la conexión",
                            "3. Revisar configuraciones de red del cliente",
                            "4. Optimizar parámetros de conexión",
                            "5. Programar monitoreo adicional por 24 horas",
                            "6. Proveer reporte de monitoreo al cliente"
                        ],
                        "escalation_needed": False,
                        "estimated_time": "20-25 minutos",
                        "follow_up_required": True
                    }
                }
            },
            "general": {
                "common_issues": [
                    "Información de cuenta",
                    "Cambio de plan",
                    "Consulta general",
                    "Solicitud de información"
                ],
                "solutions": {
                    "informacion_cuenta": {
                        "title": "Consulta de Información de Cuenta",
                        "steps": [
                            "1. Verificar identidad del cliente",
                            "2. Acceder a información de cuenta solicitada",
                            "3. Proporcionar información de manera segura",
                            "4. Explicar cualquier término o condición relevante",
                            "5. Ofrecer servicios adicionales si aplica"
                        ],
                        "escalation_needed": False,
                        "estimated_time": "5-10 minutos",
                        "follow_up_required": False
                    }
                }
            }
        }
    
    def search_knowledge_base(self, issue_type: str, specific_issue: str = "") -> Dict[str, Any]:
        """Search knowledge base for solutions"""
        issue_type_clean = issue_type.lower().strip()
        
        if issue_type_clean not in self.knowledge_base:
            return {
                "found": False,
                "message": f"No se encontró información específica para el tipo de problema: {issue_type}",
                "suggested_escalation": True,
                "available_categories": list(self.knowledge_base.keys())
            }
        
        kb_section = self.knowledge_base[issue_type_clean]
        
        result = {
            "found": True,
            "issue_type": issue_type,
            "common_issues": kb_section["common_issues"],
            "solutions": {},
            "total_solutions": len(kb_section["solutions"])
        }
        
        # Si se especifica un problema particular, buscar solución específica
        if specific_issue and specific_issue.strip():
            specific_lower = specific_issue.lower()
            for solution_key, solution_data in kb_section["solutions"].items():
                if any(keyword in specific_lower for keyword in solution_key.split("_")):
                    result["solutions"][solution_key] = solution_data
                    result["matched_solution"] = solution_key
                    break
        
        # Si no se encontró solución específica o no se proporcionó, devolver la primera disponible
        if not result["solutions"] and kb_section["solutions"]:
            first_solution_key = list(kb_section["solutions"].keys())[0]
            result["solutions"][first_solution_key] = kb_section["solutions"][first_solution_key]
            result["default_solution"] = first_solution_key
        
        return result