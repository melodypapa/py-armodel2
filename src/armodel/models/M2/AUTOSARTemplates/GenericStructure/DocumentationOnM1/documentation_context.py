"""DocumentationContext AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 327)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_DocumentationOnM1.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class DocumentationContext(MultilanguageReferrable):
    """AUTOSAR DocumentationContext."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    feature: Optional[AtpFeature]
    identifiable_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DocumentationContext."""
        super().__init__()
        self.feature: Optional[AtpFeature] = None
        self.identifiable_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DocumentationContext to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DocumentationContext, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize feature
        if self.feature is not None:
            serialized = ARObject._serialize_item(self.feature, "AtpFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FEATURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize identifiable_ref
        if self.identifiable_ref is not None:
            serialized = ARObject._serialize_item(self.identifiable_ref, "Identifiable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENTIFIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentationContext":
        """Deserialize XML element to DocumentationContext object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocumentationContext object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DocumentationContext, cls).deserialize(element)

        # Parse feature
        child = ARObject._find_child_element(element, "FEATURE")
        if child is not None:
            feature_value = ARObject._deserialize_by_tag(child, "AtpFeature")
            obj.feature = feature_value

        # Parse identifiable_ref
        child = ARObject._find_child_element(element, "IDENTIFIABLE-REF")
        if child is not None:
            identifiable_ref_value = ARRef.deserialize(child)
            obj.identifiable_ref = identifiable_ref_value

        return obj



class DocumentationContextBuilder:
    """Builder for DocumentationContext."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DocumentationContext = DocumentationContext()

    def build(self) -> DocumentationContext:
        """Build and return DocumentationContext object.

        Returns:
            DocumentationContext instance
        """
        # TODO: Add validation
        return self._obj
