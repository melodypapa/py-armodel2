"""ParameterPortAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)


class ParameterPortAnnotation(GeneralAnnotation):
    """AUTOSAR ParameterPortAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    parameter_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ParameterPortAnnotation."""
        super().__init__()
        self.parameter_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ParameterPortAnnotation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ParameterPortAnnotation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize parameter_ref
        if self.parameter_ref is not None:
            serialized = ARObject._serialize_item(self.parameter_ref, "ParameterDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PARAMETER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterPortAnnotation":
        """Deserialize XML element to ParameterPortAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ParameterPortAnnotation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ParameterPortAnnotation, cls).deserialize(element)

        # Parse parameter_ref
        child = ARObject._find_child_element(element, "PARAMETER-REF")
        if child is not None:
            parameter_ref_value = ARRef.deserialize(child)
            obj.parameter_ref = parameter_ref_value

        return obj



class ParameterPortAnnotationBuilder:
    """Builder for ParameterPortAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterPortAnnotation = ParameterPortAnnotation()

    def build(self) -> ParameterPortAnnotation:
        """Build and return ParameterPortAnnotation object.

        Returns:
            ParameterPortAnnotation instance
        """
        # TODO: Add validation
        return self._obj
