"""EvaluatedVariantSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 257)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.predefined_variant import (
    PredefinedVariant,
)


class EvaluatedVariantSet(ARElement):
    """AUTOSAR EvaluatedVariantSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    approval_status: NameToken
    evaluateds: list[PredefinedVariant]
    def __init__(self) -> None:
        """Initialize EvaluatedVariantSet."""
        super().__init__()
        self.approval_status: NameToken = None
        self.evaluateds: list[PredefinedVariant] = []
    def serialize(self) -> ET.Element:
        """Serialize EvaluatedVariantSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EvaluatedVariantSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize approval_status
        if self.approval_status is not None:
            serialized = ARObject._serialize_item(self.approval_status, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPROVAL-STATUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize evaluateds (list to container "EVALUATEDS")
        if self.evaluateds:
            wrapper = ET.Element("EVALUATEDS")
            for item in self.evaluateds:
                serialized = ARObject._serialize_item(item, "PredefinedVariant")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EvaluatedVariantSet":
        """Deserialize XML element to EvaluatedVariantSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EvaluatedVariantSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EvaluatedVariantSet, cls).deserialize(element)

        # Parse approval_status
        child = ARObject._find_child_element(element, "APPROVAL-STATUS")
        if child is not None:
            approval_status_value = child.text
            obj.approval_status = approval_status_value

        # Parse evaluateds (list from container "EVALUATEDS")
        obj.evaluateds = []
        container = ARObject._find_child_element(element, "EVALUATEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.evaluateds.append(child_value)

        return obj



class EvaluatedVariantSetBuilder:
    """Builder for EvaluatedVariantSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EvaluatedVariantSet = EvaluatedVariantSet()

    def build(self) -> EvaluatedVariantSet:
        """Build and return EvaluatedVariantSet object.

        Returns:
            EvaluatedVariantSet instance
        """
        # TODO: Add validation
        return self._obj
