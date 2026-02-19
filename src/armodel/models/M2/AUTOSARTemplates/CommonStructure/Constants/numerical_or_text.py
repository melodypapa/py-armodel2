"""NumericalOrText AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 323)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    String,
)


class NumericalOrText(ARObject):
    """AUTOSAR NumericalOrText."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    vf: Optional[Numerical]
    vt: Optional[String]
    def __init__(self) -> None:
        """Initialize NumericalOrText."""
        super().__init__()
        self.vf: Optional[Numerical] = None
        self.vt: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NumericalOrText":
        """Deserialize XML element to NumericalOrText object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NumericalOrText object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse vf
        child = ARObject._find_child_element(element, "VF")
        if child is not None:
            vf_value = child.text
            obj.vf = vf_value

        # Parse vt
        child = ARObject._find_child_element(element, "VT")
        if child is not None:
            vt_value = child.text
            obj.vt = vt_value

        return obj



class NumericalOrTextBuilder:
    """Builder for NumericalOrText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NumericalOrText = NumericalOrText()

    def build(self) -> NumericalOrText:
        """Build and return NumericalOrText object.

        Returns:
            NumericalOrText instance
        """
        # TODO: Add validation
        return self._obj
