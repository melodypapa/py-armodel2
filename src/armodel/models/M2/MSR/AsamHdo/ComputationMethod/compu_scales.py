"""CompuScales AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 388)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_content import (
    CompuContent,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale import (
    CompuScale,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization.name_converter import NameConverter


class CompuScales(CompuContent):
    """AUTOSAR CompuScales."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compu_scales: list[CompuScale]
    def __init__(self) -> None:
        """Initialize CompuScales."""
        super().__init__()
        self.compu_scales: list[CompuScale] = []

    def serialize(self) -> ET.Element:
        """Serialize CompuScales to XML element.

        AUTOSAR schema uses flat structure: COMPU-SCALES contains COMPU-SCALE items directly.

        Returns:
            xml.etree.ElementTree.Element representing this CompuScales
        """
        # Get XML tag name
        tag = NameConverter.to_xml_tag(self.__class__.__name__)
        elem = ET.Element(tag)

        # Serialize each CompuScale directly as a child element
        for scale in self.compu_scales:
            if hasattr(scale, 'serialize'):
                elem.append(scale.serialize())

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> Self:
        """Deserialize XML element to CompuScales.

        AUTOSAR schema uses flat structure: COMPU-SCALES contains COMPU-SCALE items directly.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuScales instance
        """
        # Create instance and initialize
        obj = cls.__new__(cls)
        obj.__init__()

        # Find all COMPU-SCALE child elements directly
        for child in element:
            child_tag = ARObject._strip_namespace(child.tag)
            if child_tag == "COMPU-SCALE":
                if hasattr(CompuScale, 'deserialize'):
                    scale = ARObject._unwrap_primitive(CompuScale.deserialize(child))
                    obj.compu_scales.append(scale)

        return obj


class CompuScalesBuilder:
    """Builder for CompuScales."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuScales = CompuScales()

    def build(self) -> CompuScales:
        """Build and return CompuScales object.

        Returns:
            CompuScales instance
        """
        # TODO: Add validation
        return self._obj