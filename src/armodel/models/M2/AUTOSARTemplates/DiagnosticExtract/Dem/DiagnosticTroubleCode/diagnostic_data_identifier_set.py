"""DiagnosticDataIdentifierSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 187)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_identifier import (
    DiagnosticDataIdentifier,
)


class DiagnosticDataIdentifierSet(DiagnosticCommonElement):
    """AUTOSAR DiagnosticDataIdentifierSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_identifier_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticDataIdentifierSet."""
        super().__init__()
        self.data_identifier_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDataIdentifierSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDataIdentifierSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_identifier_refs (list to container "DATA-IDENTIFIER-REFS")
        if self.data_identifier_refs:
            wrapper = ET.Element("DATA-IDENTIFIER-REFS")
            for item in self.data_identifier_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticDataIdentifier")
                if serialized is not None:
                    child_elem = ET.Element("DATA-IDENTIFIER-REF")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataIdentifierSet":
        """Deserialize XML element to DiagnosticDataIdentifierSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDataIdentifierSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDataIdentifierSet, cls).deserialize(element)

        # Parse data_identifier_refs (list from container "DATA-IDENTIFIER-REFS")
        obj.data_identifier_refs = []
        container = SerializationHelper.find_child_element(element, "DATA-IDENTIFIER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_identifier_refs.append(child_value)

        return obj



class DiagnosticDataIdentifierSetBuilder:
    """Builder for DiagnosticDataIdentifierSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataIdentifierSet = DiagnosticDataIdentifierSet()

    def build(self) -> DiagnosticDataIdentifierSet:
        """Build and return DiagnosticDataIdentifierSet object.

        Returns:
            DiagnosticDataIdentifierSet instance
        """
        # TODO: Add validation
        return self._obj
