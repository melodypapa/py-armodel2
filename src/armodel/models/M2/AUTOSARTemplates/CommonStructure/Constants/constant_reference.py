"""ConstantReference AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 440)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)


class ConstantReference(ValueSpecification):
    """AUTOSAR ConstantReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    constant: Optional[ConstantSpecification]
    def __init__(self) -> None:
        """Initialize ConstantReference."""
        super().__init__()
        self.constant: Optional[ConstantSpecification] = None
    def serialize(self) -> ET.Element:
        """Serialize ConstantReference to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConstantReference, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize constant
        if self.constant is not None:
            serialized = ARObject._serialize_item(self.constant, "ConstantSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONSTANT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstantReference":
        """Deserialize XML element to ConstantReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConstantReference object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConstantReference, cls).deserialize(element)

        # Parse constant
        child = ARObject._find_child_element(element, "CONSTANT")
        if child is not None:
            constant_value = ARObject._deserialize_by_tag(child, "ConstantSpecification")
            obj.constant = constant_value

        return obj



class ConstantReferenceBuilder:
    """Builder for ConstantReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConstantReference = ConstantReference()

    def build(self) -> ConstantReference:
        """Build and return ConstantReference object.

        Returns:
            ConstantReference instance
        """
        # TODO: Add validation
        return self._obj
