"""ApplicationValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 299)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue.sw_axis_cont import (
    SwAxisCont,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue.sw_value_cont import (
    SwValueCont,
)


class ApplicationValueSpecification(ValueSpecification):
    """AUTOSAR ApplicationValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category: Optional[Identifier]
    sw_axis_conts: list[SwAxisCont]
    sw_value_cont: Optional[SwValueCont]
    def __init__(self) -> None:
        """Initialize ApplicationValueSpecification."""
        super().__init__()
        self.category: Optional[Identifier] = None
        self.sw_axis_conts: list[SwAxisCont] = []
        self.sw_value_cont: Optional[SwValueCont] = None
    def serialize(self) -> ET.Element:
        """Serialize ApplicationValueSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationValueSpecification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize category
        if self.category is not None:
            serialized = ARObject._serialize_item(self.category, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_axis_conts (list to container "SW-AXIS-CONTS")
        if self.sw_axis_conts:
            wrapper = ET.Element("SW-AXIS-CONTS")
            for item in self.sw_axis_conts:
                serialized = ARObject._serialize_item(item, "SwAxisCont")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_value_cont
        if self.sw_value_cont is not None:
            serialized = ARObject._serialize_item(self.sw_value_cont, "SwValueCont")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-VALUE-CONT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationValueSpecification":
        """Deserialize XML element to ApplicationValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationValueSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationValueSpecification, cls).deserialize(element)

        # Parse category
        child = ARObject._find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.category = category_value

        # Parse sw_axis_conts (list from container "SW-AXIS-CONTS")
        obj.sw_axis_conts = []
        container = ARObject._find_child_element(element, "SW-AXIS-CONTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_axis_conts.append(child_value)

        # Parse sw_value_cont
        child = ARObject._find_child_element(element, "SW-VALUE-CONT")
        if child is not None:
            sw_value_cont_value = ARObject._deserialize_by_tag(child, "SwValueCont")
            obj.sw_value_cont = sw_value_cont_value

        return obj



class ApplicationValueSpecificationBuilder:
    """Builder for ApplicationValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationValueSpecification = ApplicationValueSpecification()

    def build(self) -> ApplicationValueSpecification:
        """Build and return ApplicationValueSpecification object.

        Returns:
            ApplicationValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
