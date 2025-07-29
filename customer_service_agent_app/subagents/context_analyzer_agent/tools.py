from typing import Dict, List, Any
from datetime import datetime

class CustomerContextTool:
    """Tool for analyzing customer context and interaction history"""
    
    def __init__(self):
        # Simulación de base de datos de clientes
        self.customer_db = {
            "CUST_001": {
                "name": "María González",
                "tier": "Premium",
                "join_date": "2022-03-15",
                "total_interactions": 12,
                "recent_issues": ["facturación", "técnico", "facturación"],
                "satisfaction_score": 4.2,
                "last_interaction": "2024-01-15",
                "preferred_channel": "chat",
                "language": "es"
            },
            "CUST_002": {
                "name": "Juan Pérez",
                "tier": "Basic",
                "join_date": "2023-08-20",
                "total_interactions": 3,
                "recent_issues": ["técnico"],
                "satisfaction_score": 3.8,
                "last_interaction": "2024-01-10",
                "preferred_channel": "email",
                "language": "es"
            },
            "CUST_003": {
                "name": "Ana López",
                "tier": "Gold",
                "join_date": "2021-11-08",
                "total_interactions": 8,
                "recent_issues": ["facturación", "general", "técnico"],
                "satisfaction_score": 4.5,
                "last_interaction": "2024-01-20",
                "preferred_channel": "phone",
                "language": "es"
            }
        }
    
    def get_customer_context(self, customer_id: str) -> Dict[str, Any]:
        """Retrieve complete customer context"""
        customer_data = self.customer_db.get(customer_id, {})
        
        if not customer_data:
            return {
                "error": f"Customer {customer_id} not found",
                "customer_id": customer_id,
                "suggestion": "Please verify customer ID or ask customer to provide correct identification"
            }
        
        # Calcular métricas adicionales
        try:
            days_since_last = (datetime.now() - datetime.fromisoformat(customer_data["last_interaction"])).days
        except:
            days_since_last = 0
            
        is_frequent_user = customer_data["total_interactions"] > 5
        is_vip = customer_data["tier"] in ["Premium", "Gold"]
        
        return {
            "customer_id": customer_id,
            "customer_data": customer_data,
            "calculated_metrics": {
                "days_since_last_interaction": days_since_last,
                "is_frequent_user": is_frequent_user,
                "is_vip_customer": is_vip,
                "risk_level": "high" if customer_data["satisfaction_score"] < 3.5 else "low",
                "tier_priority": {"Premium": 3, "Gold": 2, "Basic": 1}.get(customer_data["tier"], 1)
            }
        }