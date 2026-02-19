"""ArrayValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 303)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 434)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1999)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import (
    CompositeValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class ArrayValueSpecification(CompositeValueSpecification):
    """AUTOSAR ArrayValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    elements: list[ValueSpecification]
    intended_partial: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ArrayValueSpecification."""
        super().__init__()
        self.elements: list[ValueSpecification] = []
        self.intended_partial: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize ArrayValueSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ArrayValueSpecification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize elements (list to container "ELEMENTS")
        if self.elements:
            wrapper = ET.Element("ELEMENTS")
            for item in self.elements:
                serialized = ARObject._serialize_item(item, "ValueSpecification")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize intended_partial
        if self.intended_partial is not None:
            serialized = ARObject._serialize_item(self.intended_partial, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTENDED-PARTIAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArrayValueSpecification":
        """Deserialize XML element to ArrayValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ArrayValueSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ArrayValueSpecification, cls).deserialize(element)

        # Parse elements (list from container "ELEMENTS")
        obj.elements = []
        container = ARObject._find_child_element(element, "ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.elements.append(child_value)

        # Parse intended_partial
        child = ARObject._find_child_element(element, "INTENDED-PARTIAL")
        if child is not None:
            intended_partial_value = child.text
            obj.intended_partial = intended_partial_value

        return obj



class ArrayValueSpecificationBuilder:
    """Builder for ArrayValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArrayValueSpecification = ArrayValueSpecification()

    def build(self) -> ArrayValueSpecification:
        """Build and return ArrayValueSpecification object.

        Returns:
            ArrayValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
