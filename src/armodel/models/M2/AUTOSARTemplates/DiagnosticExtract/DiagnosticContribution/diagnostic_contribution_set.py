"""DiagnosticContributionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 56)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticContribution.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution.diagnostic_service_table import (
    DiagnosticServiceTable,
)


class DiagnosticContributionSet(ARElement):
    """AUTOSAR DiagnosticContributionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    common: Optional[Any]
    element_refs: list[Any]
    service_table_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticContributionSet."""
        super().__init__()
        self.common: Optional[Any] = None
        self.element_refs: list[Any] = []
        self.service_table_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticContributionSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticContributionSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize common
        if self.common is not None:
            serialized = ARObject._serialize_item(self.common, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMON")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize element_refs (list to container "ELEMENT-REFS")
        if self.element_refs:
            wrapper = ET.Element("ELEMENT-REFS")
            for item in self.element_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize service_table_refs (list to container "SERVICE-TABLE-REFS")
        if self.service_table_refs:
            wrapper = ET.Element("SERVICE-TABLE-REFS")
            for item in self.service_table_refs:
                serialized = ARObject._serialize_item(item, "DiagnosticServiceTable")
                if serialized is not None:
                    child_elem = ET.Element("SERVICE-TABLE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticContributionSet":
        """Deserialize XML element to DiagnosticContributionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticContributionSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticContributionSet, cls).deserialize(element)

        # Parse common
        child = ARObject._find_child_element(element, "COMMON")
        if child is not None:
            common_value = child.text
            obj.common = common_value

        # Parse element_refs (list from container "ELEMENT-REFS")
        obj.element_refs = []
        container = ARObject._find_child_element(element, "ELEMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.element_refs.append(child_value)

        # Parse service_table_refs (list from container "SERVICE-TABLE-REFS")
        obj.service_table_refs = []
        container = ARObject._find_child_element(element, "SERVICE-TABLE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.service_table_refs.append(child_value)

        return obj



class DiagnosticContributionSetBuilder:
    """Builder for DiagnosticContributionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticContributionSet = DiagnosticContributionSet()

    def build(self) -> DiagnosticContributionSet:
        """Build and return DiagnosticContributionSet object.

        Returns:
            DiagnosticContributionSet instance
        """
        # TODO: Add validation
        return self._obj
