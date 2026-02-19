"""EcucAddInfoParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 68)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class EcucAddInfoParamDef(EcucParameterDef):
    """AUTOSAR EcucAddInfoParamDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize EcucAddInfoParamDef."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize EcucAddInfoParamDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucAddInfoParamDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAddInfoParamDef":
        """Deserialize XML element to EcucAddInfoParamDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucAddInfoParamDef object
        """
        # Delegate to parent class to handle inherited attributes
        return super(EcucAddInfoParamDef, cls).deserialize(element)



class EcucAddInfoParamDefBuilder:
    """Builder for EcucAddInfoParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAddInfoParamDef = EcucAddInfoParamDef()

    def build(self) -> EcucAddInfoParamDef:
        """Build and return EcucAddInfoParamDef object.

        Returns:
            EcucAddInfoParamDef instance
        """
        # TODO: Add validation
        return self._obj
