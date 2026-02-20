"""RptServicePoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 206)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    PositiveInteger,
)


class RptServicePoint(Identifiable):
    """AUTOSAR RptServicePoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    service_id: Optional[PositiveInteger]
    symbol: Optional[CIdentifier]
    def __init__(self) -> None:
        """Initialize RptServicePoint."""
        super().__init__()
        self.service_id: Optional[PositiveInteger] = None
        self.symbol: Optional[CIdentifier] = None

    def serialize(self) -> ET.Element:
        """Serialize RptServicePoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptServicePoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize service_id
        if self.service_id is not None:
            serialized = ARObject._serialize_item(self.service_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize symbol
        if self.symbol is not None:
            serialized = ARObject._serialize_item(self.symbol, "CIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptServicePoint":
        """Deserialize XML element to RptServicePoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptServicePoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptServicePoint, cls).deserialize(element)

        # Parse service_id
        child = ARObject._find_child_element(element, "SERVICE-ID")
        if child is not None:
            service_id_value = child.text
            obj.service_id = service_id_value

        # Parse symbol
        child = ARObject._find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = ARObject._deserialize_by_tag(child, "CIdentifier")
            obj.symbol = symbol_value

        return obj



class RptServicePointBuilder:
    """Builder for RptServicePoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptServicePoint = RptServicePoint()

    def build(self) -> RptServicePoint:
        """Build and return RptServicePoint object.

        Returns:
            RptServicePoint instance
        """
        # TODO: Add validation
        return self._obj
