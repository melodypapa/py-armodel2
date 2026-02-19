"""EcucEnumerationLiteralDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 67)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class EcucEnumerationLiteralDef(Identifiable):
    """AUTOSAR EcucEnumerationLiteralDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecuc_cond: Optional[Any]
    origin: Optional[String]
    def __init__(self) -> None:
        """Initialize EcucEnumerationLiteralDef."""
        super().__init__()
        self.ecuc_cond: Optional[Any] = None
        self.origin: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucEnumerationLiteralDef":
        """Deserialize XML element to EcucEnumerationLiteralDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucEnumerationLiteralDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucEnumerationLiteralDef, cls).deserialize(element)

        # Parse ecuc_cond
        child = ARObject._find_child_element(element, "ECUC-COND")
        if child is not None:
            ecuc_cond_value = child.text
            obj.ecuc_cond = ecuc_cond_value

        # Parse origin
        child = ARObject._find_child_element(element, "ORIGIN")
        if child is not None:
            origin_value = child.text
            obj.origin = origin_value

        return obj



class EcucEnumerationLiteralDefBuilder:
    """Builder for EcucEnumerationLiteralDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucEnumerationLiteralDef = EcucEnumerationLiteralDef()

    def build(self) -> EcucEnumerationLiteralDef:
        """Build and return EcucEnumerationLiteralDef object.

        Returns:
            EcucEnumerationLiteralDef instance
        """
        # TODO: Add validation
        return self._obj
