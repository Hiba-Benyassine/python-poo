class Compte:
    def __init__(self, account_number: str, account_holder: str, solde_du_compte: float = 0.0):
        #Constructeur
        self.account_number = account_number
        self.account_holder = account_holder
        self.solde_du_compte = solde_du_compte

    def deposit(self, amount: float):

        if amount > 0:
            self.solde_du_compte += amount
            print(f"{amount} dh déposés. Nouveau solde: {self.solde_du_compte} dh")
        else:
            print(" Le montant du dépôt doit être positif.")

    def retirer(self, montant: float):
        """
        Retirer de l'argent du compte (si le solde est suffisant)
        """
        if montant > 0:
            if self.solde_du_compte >= montant:
                self.solde_du_compte -= montant
                print(f"{montant}  retirés. Nouveau solde: {self.solde_du_compte} dh")
            else:
                print(" Fonds insuffisants pour effectuer ce retrait.")
        else:
            print(" Le montant du retrait doit être positif.")

    def check_balance(self):
        """
        Vérifier le solde du compte
        """
        print(f" Solde actuel du compte: {self.solde_du_compte} dh")
        return self.solde_du_compte

if __name__ == "__main__":
    # Création d’un compte principal
    my_account = Compte("123456789", "Hiba", 500.0)

    # Dépôt
    my_account.deposit(200.0)

    # Retrait
    my_account.retirer(100.0)

    # Vérification solde
    my_account.check_balance()

    print("\n--- Création de plusieurs comptes ---\n")

    # Création de plusieurs comptes
    compte1 = Compte("111111", "Ali", 1000.0)
    compte2 = Compte("222222", "Sara", 50.0)

    # Transactions sur compte1
    compte1.deposit(500)
    compte1.retirer(200)
    compte1.check_balance()

    # Transactions sur compte2
    compte2.deposit(100)
    compte2.retirer(200)  # Fonds insuffisants
    compte2.check_balance()
