"""AutosarVariableInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 85)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class AutosarVariableInstance(Identifiable):
    """AUTOSAR AutosarVariableInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    variable_instance_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize AutosarVariableInstance."""
        super().__init__()
        self.variable_instance_instance_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize AutosarVariableInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AutosarVariableInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize variable_instance_instance_ref
        if self.variable_instance_instance_ref is not None:
            serialized = ARObject._serialize_item(self.variable_instance_instance_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIABLE-INSTANCE-INSTANCE-REF-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AutosarVariableInstance":
        """Deserialize XML element to AutosarVariableInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AutosarVariableInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AutosarVariableInstance, cls).deserialize(element)

        # Parse variable_instance_instance_ref
        child = ARObject._find_child_element(element, "VARIABLE-INSTANCE-INSTANCE-REF-REF")
        if child is not None:
            variable_instance_instance_ref_value = ARRef.deserialize(child)
            obj.variable_instance_instance_ref = variable_instance_instance_ref_value

        return obj



class AutosarVariableInstanceBuilder:
    """Builder for AutosarVariableInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarVariableInstance = AutosarVariableInstance()

    def build(self) -> AutosarVariableInstance:
        """Build and return AutosarVariableInstance object.

        Returns:
            AutosarVariableInstance instance
        """
        # TODO: Add validation
        return self._obj
