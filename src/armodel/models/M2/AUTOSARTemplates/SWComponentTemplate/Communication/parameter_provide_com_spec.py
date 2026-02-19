"""ParameterProvideComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 192)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class ParameterProvideComSpec(PPortComSpec):
    """AUTOSAR ParameterProvideComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    init_value: Optional[ValueSpecification]
    parameter_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ParameterProvideComSpec."""
        super().__init__()
        self.init_value: Optional[ValueSpecification] = None
        self.parameter_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ParameterProvideComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ParameterProvideComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize init_value
        if self.init_value is not None:
            serialized = ARObject._serialize_item(self.init_value, "ValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INIT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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
    def deserialize(cls, element: ET.Element) -> "ParameterProvideComSpec":
        """Deserialize XML element to ParameterProvideComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ParameterProvideComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ParameterProvideComSpec, cls).deserialize(element)

        # Parse init_value
        child = ARObject._find_child_element(element, "INIT-VALUE")
        if child is not None:
            init_value_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.init_value = init_value_value

        # Parse parameter_ref
        child = ARObject._find_child_element(element, "PARAMETER-REF")
        if child is not None:
            parameter_ref_value = ARRef.deserialize(child)
            obj.parameter_ref = parameter_ref_value

        return obj



class ParameterProvideComSpecBuilder:
    """Builder for ParameterProvideComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterProvideComSpec = ParameterProvideComSpec()

    def build(self) -> ParameterProvideComSpec:
        """Build and return ParameterProvideComSpec object.

        Returns:
            ParameterProvideComSpec instance
        """
        # TODO: Add validation
        return self._obj
