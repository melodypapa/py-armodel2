"""DiagnosticParameter AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 36)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_abstract_parameter import (
    DiagnosticAbstractParameter,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticParameter(DiagnosticAbstractParameter):
    """AUTOSAR DiagnosticParameter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ident: Optional[DiagnosticParameter]
    support_info: Optional[DiagnosticParameter]
    def __init__(self) -> None:
        """Initialize DiagnosticParameter."""
        super().__init__()
        self.ident: Optional[DiagnosticParameter] = None
        self.support_info: Optional[DiagnosticParameter] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticParameter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticParameter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ident
        if self.ident is not None:
            serialized = ARObject._serialize_item(self.ident, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize support_info
        if self.support_info is not None:
            serialized = ARObject._serialize_item(self.support_info, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORT-INFO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameter":
        """Deserialize XML element to DiagnosticParameter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticParameter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticParameter, cls).deserialize(element)

        # Parse ident
        child = ARObject._find_child_element(element, "IDENT")
        if child is not None:
            ident_value = ARObject._deserialize_by_tag(child, "DiagnosticParameter")
            obj.ident = ident_value

        # Parse support_info
        child = ARObject._find_child_element(element, "SUPPORT-INFO")
        if child is not None:
            support_info_value = ARObject._deserialize_by_tag(child, "DiagnosticParameter")
            obj.support_info = support_info_value

        return obj



class DiagnosticParameterBuilder:
    """Builder for DiagnosticParameter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameter = DiagnosticParameter()

    def build(self) -> DiagnosticParameter:
        """Build and return DiagnosticParameter object.

        Returns:
            DiagnosticParameter instance
        """
        # TODO: Add validation
        return self._obj
