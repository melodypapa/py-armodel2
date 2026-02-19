"""CompuScaleConstantContents AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 390)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_contents import (
    CompuScaleContents,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import (
    CompuConst,
)


class CompuScaleConstantContents(CompuScaleContents):
    """AUTOSAR CompuScaleConstantContents."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compu_const: Optional[CompuConst]
    def __init__(self) -> None:
        """Initialize CompuScaleConstantContents."""
        super().__init__()
        self.compu_const: Optional[CompuConst] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuScaleConstantContents":
        """Deserialize XML element to CompuScaleConstantContents object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuScaleConstantContents object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse compu_const
        child = ARObject._find_child_element(element, "COMPU-CONST")
        if child is not None:
            compu_const_value = ARObject._deserialize_by_tag(child, "CompuConst")
            obj.compu_const = compu_const_value

        return obj



class CompuScaleConstantContentsBuilder:
    """Builder for CompuScaleConstantContents."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuScaleConstantContents = CompuScaleConstantContents()

    def build(self) -> CompuScaleConstantContents:
        """Build and return CompuScaleConstantContents object.

        Returns:
            CompuScaleConstantContents instance
        """
        # TODO: Add validation
        return self._obj
