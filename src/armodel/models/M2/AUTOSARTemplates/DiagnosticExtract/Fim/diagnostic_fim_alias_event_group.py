"""DiagnosticFimAliasEventGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 263)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_abstract_alias_event import (
    DiagnosticAbstractAliasEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticFimAliasEventGroup(DiagnosticAbstractAliasEvent):
    """AUTOSAR DiagnosticFimAliasEventGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    grouped_aliases: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticFimAliasEventGroup."""
        super().__init__()
        self.grouped_aliases: list[Any] = []
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticFimAliasEventGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticFimAliasEventGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize grouped_aliases (list to container "GROUPED-ALIASES")
        if self.grouped_aliases:
            wrapper = ET.Element("GROUPED-ALIASES")
            for item in self.grouped_aliases:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimAliasEventGroup":
        """Deserialize XML element to DiagnosticFimAliasEventGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFimAliasEventGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticFimAliasEventGroup, cls).deserialize(element)

        # Parse grouped_aliases (list from container "GROUPED-ALIASES")
        obj.grouped_aliases = []
        container = ARObject._find_child_element(element, "GROUPED-ALIASES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.grouped_aliases.append(child_value)

        return obj



class DiagnosticFimAliasEventGroupBuilder:
    """Builder for DiagnosticFimAliasEventGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimAliasEventGroup = DiagnosticFimAliasEventGroup()

    def build(self) -> DiagnosticFimAliasEventGroup:
        """Build and return DiagnosticFimAliasEventGroup object.

        Returns:
            DiagnosticFimAliasEventGroup instance
        """
        # TODO: Add validation
        return self._obj
