"""TlsCryptoCipherSuiteProps AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class TlsCryptoCipherSuiteProps(Identifiable):
    """AUTOSAR TlsCryptoCipherSuiteProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tcp_ip_tls_use": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpTlsUse
    }

    def __init__(self) -> None:
        """Initialize TlsCryptoCipherSuiteProps."""
        super().__init__()
        self.tcp_ip_tls_use: Optional[Boolean] = None


class TlsCryptoCipherSuitePropsBuilder:
    """Builder for TlsCryptoCipherSuiteProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TlsCryptoCipherSuiteProps = TlsCryptoCipherSuiteProps()

    def build(self) -> TlsCryptoCipherSuiteProps:
        """Build and return TlsCryptoCipherSuiteProps object.

        Returns:
            TlsCryptoCipherSuiteProps instance
        """
        # TODO: Add validation
        return self._obj
