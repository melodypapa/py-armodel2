"""CompuScales AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 388)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_content import (
    CompuContent,
)
from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale import (
    CompuScale,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
from armodel2.serialization.name_converter import NameConverter


class CompuScales(CompuContent):
    """AUTOSAR CompuScales."""

    _XML_TAG = "COMPU-SCALES"

    _DESERIALIZE_DISPATCH = {
        "COMPU-SCALE": lambda obj, elem: obj.compu_scales.append(
            SerializationHelper.unwrap_primitive(CompuScale.deserialize(elem))
        ),
    }

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
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes (checksum, timestamp)
        parent_elem = super(CompuScales, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize each CompuScale directly as a child element
        for scale in self.compu_scales:
            if hasattr(scale, 'serialize'):
                elem.append(scale.serialize())

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuScales":
        """Deserialize XML element to CompuScales.

        AUTOSAR schema uses flat structure: COMPU-SCALES contains COMPU-SCALE items directly.
        Uses static dispatch table for O(1) tag-to-handler lookup.
        Calls super().deserialize() first to handle inherited attributes from CompuContent -> ARObject.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuScales instance
        """
        # First, deserialize inherited attributes from parent chain (CompuContent -> ARObject)
        obj = super(CompuScales, cls).deserialize(element)

        # Then process CompuScales-specific elements with dispatch table
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            handler = cls._DESERIALIZE_DISPATCH.get(tag)
            if handler is not None:
                handler(obj, child)

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
        return self._obj