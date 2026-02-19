"""NvDataPortAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class NvDataPortAnnotation(GeneralAnnotation):
    """AUTOSAR NvDataPortAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    variable_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize NvDataPortAnnotation."""
        super().__init__()
        self.variable_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize NvDataPortAnnotation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NvDataPortAnnotation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize variable_ref
        if self.variable_ref is not None:
            serialized = ARObject._serialize_item(self.variable_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvDataPortAnnotation":
        """Deserialize XML element to NvDataPortAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvDataPortAnnotation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NvDataPortAnnotation, cls).deserialize(element)

        # Parse variable_ref
        child = ARObject._find_child_element(element, "VARIABLE-REF")
        if child is not None:
            variable_ref_value = ARRef.deserialize(child)
            obj.variable_ref = variable_ref_value

        return obj



class NvDataPortAnnotationBuilder:
    """Builder for NvDataPortAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvDataPortAnnotation = NvDataPortAnnotation()

    def build(self) -> NvDataPortAnnotation:
        """Build and return NvDataPortAnnotation object.

        Returns:
            NvDataPortAnnotation instance
        """
        # TODO: Add validation
        return self._obj
