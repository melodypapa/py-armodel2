"""UserDefinedPdu AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class UserDefinedPdu(Pdu):
    """AUTOSAR UserDefinedPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "cdd_type": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # cddType
    }

    def __init__(self) -> None:
        """Initialize UserDefinedPdu."""
        super().__init__()
        self.cdd_type: Optional[String] = None


class UserDefinedPduBuilder:
    """Builder for UserDefinedPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedPdu = UserDefinedPdu()

    def build(self) -> UserDefinedPdu:
        """Build and return UserDefinedPdu object.

        Returns:
            UserDefinedPdu instance
        """
        # TODO: Add validation
        return self._obj
