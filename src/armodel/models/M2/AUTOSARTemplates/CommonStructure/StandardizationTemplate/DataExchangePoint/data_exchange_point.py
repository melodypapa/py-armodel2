"""DataExchangePoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 78)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.baseline import (
    Baseline,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.data_format_tailoring import (
    DataFormatTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.specification_scope import (
    SpecificationScope,
)


class DataExchangePoint(ARElement):
    """AUTOSAR DataExchangePoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_format: Optional[DataFormatTailoring]
    kind: DataExchangePoint
    referenced: Baseline
    specification_scope: Optional[SpecificationScope]
    def __init__(self) -> None:
        """Initialize DataExchangePoint."""
        super().__init__()
        self.data_format: Optional[DataFormatTailoring] = None
        self.kind: DataExchangePoint = None
        self.referenced: Baseline = None
        self.specification_scope: Optional[SpecificationScope] = None

    def serialize(self) -> ET.Element:
        """Serialize DataExchangePoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataExchangePoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_format
        if self.data_format is not None:
            serialized = ARObject._serialize_item(self.data_format, "DataFormatTailoring")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-FORMAT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize kind
        if self.kind is not None:
            serialized = ARObject._serialize_item(self.kind, "DataExchangePoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize referenced
        if self.referenced is not None:
            serialized = ARObject._serialize_item(self.referenced, "Baseline")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFERENCED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize specification_scope
        if self.specification_scope is not None:
            serialized = ARObject._serialize_item(self.specification_scope, "SpecificationScope")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SPECIFICATION-SCOPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataExchangePoint":
        """Deserialize XML element to DataExchangePoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataExchangePoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataExchangePoint, cls).deserialize(element)

        # Parse data_format
        child = ARObject._find_child_element(element, "DATA-FORMAT")
        if child is not None:
            data_format_value = ARObject._deserialize_by_tag(child, "DataFormatTailoring")
            obj.data_format = data_format_value

        # Parse kind
        child = ARObject._find_child_element(element, "KIND")
        if child is not None:
            kind_value = ARObject._deserialize_by_tag(child, "DataExchangePoint")
            obj.kind = kind_value

        # Parse referenced
        child = ARObject._find_child_element(element, "REFERENCED")
        if child is not None:
            referenced_value = ARObject._deserialize_by_tag(child, "Baseline")
            obj.referenced = referenced_value

        # Parse specification_scope
        child = ARObject._find_child_element(element, "SPECIFICATION-SCOPE")
        if child is not None:
            specification_scope_value = ARObject._deserialize_by_tag(child, "SpecificationScope")
            obj.specification_scope = specification_scope_value

        return obj



class DataExchangePointBuilder:
    """Builder for DataExchangePoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataExchangePoint = DataExchangePoint()

    def build(self) -> DataExchangePoint:
        """Build and return DataExchangePoint object.

        Returns:
            DataExchangePoint instance
        """
        # TODO: Add validation
        return self._obj
