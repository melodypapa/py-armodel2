"""UserDefinedIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 346)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class UserDefinedIPdu(IPdu):
    """AUTOSAR UserDefinedIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cdd_type: Optional[String]
    def __init__(self) -> None:
        """Initialize UserDefinedIPdu."""
        super().__init__()
        self.cdd_type: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedIPdu":
        """Deserialize XML element to UserDefinedIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UserDefinedIPdu object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse cdd_type
        child = ARObject._find_child_element(element, "CDD-TYPE")
        if child is not None:
            cdd_type_value = child.text
            obj.cdd_type = cdd_type_value

        return obj



class UserDefinedIPduBuilder:
    """Builder for UserDefinedIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedIPdu = UserDefinedIPdu()

    def build(self) -> UserDefinedIPdu:
        """Build and return UserDefinedIPdu object.

        Returns:
            UserDefinedIPdu instance
        """
        # TODO: Add validation
        return self._obj
