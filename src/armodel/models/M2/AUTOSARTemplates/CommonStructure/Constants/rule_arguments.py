"""RuleArguments AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 329)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.numerical_or_text import (
    NumericalOrText,
)


class RuleArguments(ARObject):
    """AUTOSAR RuleArguments."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    v: Optional[Numerical]
    vf: Optional[Numerical]
    vt: Optional[VerbatimString]
    vtf: Optional[NumericalOrText]
    def __init__(self) -> None:
        """Initialize RuleArguments."""
        super().__init__()
        self.v: Optional[Numerical] = None
        self.vf: Optional[Numerical] = None
        self.vt: Optional[VerbatimString] = None
        self.vtf: Optional[NumericalOrText] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RuleArguments":
        """Deserialize XML element to RuleArguments object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RuleArguments object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse v
        child = ARObject._find_child_element(element, "V")
        if child is not None:
            v_value = child.text
            obj.v = v_value

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

        # Parse vtf
        child = ARObject._find_child_element(element, "VTF")
        if child is not None:
            vtf_value = ARObject._deserialize_by_tag(child, "NumericalOrText")
            obj.vtf = vtf_value

        return obj



class RuleArgumentsBuilder:
    """Builder for RuleArguments."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RuleArguments = RuleArguments()

    def build(self) -> RuleArguments:
        """Build and return RuleArguments object.

        Returns:
            RuleArguments instance
        """
        # TODO: Add validation
        return self._obj
