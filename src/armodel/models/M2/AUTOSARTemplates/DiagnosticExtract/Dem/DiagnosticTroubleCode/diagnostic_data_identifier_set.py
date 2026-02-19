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

    data_identifiers: list[DiagnosticDataIdentifier]
    def __init__(self) -> None:
        """Initialize DiagnosticDataIdentifierSet."""
        super().__init__()
        self.data_identifiers: list[DiagnosticDataIdentifier] = []
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDataIdentifierSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDataIdentifierSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_identifiers (list to container "DATA-IDENTIFIERS")
        if self.data_identifiers:
            wrapper = ET.Element("DATA-IDENTIFIERS")
            for item in self.data_identifiers:
                serialized = ARObject._serialize_item(item, "DiagnosticDataIdentifier")
                if serialized is not None:
                    wrapper.append(serialized)
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

        # Parse data_identifiers (list from container "DATA-IDENTIFIERS")
        obj.data_identifiers = []
        container = ARObject._find_child_element(element, "DATA-IDENTIFIERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_identifiers.append(child_value)

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
