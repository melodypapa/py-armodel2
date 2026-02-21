"""PostBuildVariantCriterion AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 304)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 614)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 76)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 232)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_method import (
    CompuMethod,
)


class PostBuildVariantCriterion(ARElement):
    """AUTOSAR PostBuildVariantCriterion."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compu_method_ref: ARRef
    def __init__(self) -> None:
        """Initialize PostBuildVariantCriterion."""
        super().__init__()
        self.compu_method_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize PostBuildVariantCriterion to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PostBuildVariantCriterion, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize compu_method_ref
        if self.compu_method_ref is not None:
            serialized = SerializationHelper.serialize_item(self.compu_method_ref, "CompuMethod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPU-METHOD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PostBuildVariantCriterion":
        """Deserialize XML element to PostBuildVariantCriterion object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PostBuildVariantCriterion object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PostBuildVariantCriterion, cls).deserialize(element)

        # Parse compu_method_ref
        child = SerializationHelper.find_child_element(element, "COMPU-METHOD-REF")
        if child is not None:
            compu_method_ref_value = ARRef.deserialize(child)
            obj.compu_method_ref = compu_method_ref_value

        return obj



class PostBuildVariantCriterionBuilder:
    """Builder for PostBuildVariantCriterion."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PostBuildVariantCriterion = PostBuildVariantCriterion()

    def build(self) -> PostBuildVariantCriterion:
        """Build and return PostBuildVariantCriterion object.

        Returns:
            PostBuildVariantCriterion instance
        """
        # TODO: Add validation
        return self._obj
