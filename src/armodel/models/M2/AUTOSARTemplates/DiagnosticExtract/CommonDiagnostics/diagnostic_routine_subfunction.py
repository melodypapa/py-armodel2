"""DiagnosticRoutineSubfunction AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 121)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
    DiagnosticAccessPermission,
)
from abc import ABC, abstractmethod


class DiagnosticRoutineSubfunction(Identifiable, ABC):
    """AUTOSAR DiagnosticRoutineSubfunction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    access: Optional[DiagnosticAccessPermission]
    def __init__(self) -> None:
        """Initialize DiagnosticRoutineSubfunction."""
        super().__init__()
        self.access: Optional[DiagnosticAccessPermission] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRoutineSubfunction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRoutineSubfunction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize access
        if self.access is not None:
            serialized = ARObject._serialize_item(self.access, "DiagnosticAccessPermission")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRoutineSubfunction":
        """Deserialize XML element to DiagnosticRoutineSubfunction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRoutineSubfunction object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRoutineSubfunction, cls).deserialize(element)

        # Parse access
        child = ARObject._find_child_element(element, "ACCESS")
        if child is not None:
            access_value = ARObject._deserialize_by_tag(child, "DiagnosticAccessPermission")
            obj.access = access_value

        return obj



class DiagnosticRoutineSubfunctionBuilder:
    """Builder for DiagnosticRoutineSubfunction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutineSubfunction = DiagnosticRoutineSubfunction()

    def build(self) -> DiagnosticRoutineSubfunction:
        """Build and return DiagnosticRoutineSubfunction object.

        Returns:
            DiagnosticRoutineSubfunction instance
        """
        # TODO: Add validation
        return self._obj
