"""EcucDestinationUriPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 83)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)


class EcucDestinationUriPolicy(ARObject):
    """AUTOSAR EcucDestinationUriPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    containers: list[EcucContainerDef]
    destination_uri: Optional[Any]
    parameters: list[EcucParameterDef]
    reference_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize EcucDestinationUriPolicy."""
        super().__init__()
        self.containers: list[EcucContainerDef] = []
        self.destination_uri: Optional[Any] = None
        self.parameters: list[EcucParameterDef] = []
        self.reference_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDestinationUriPolicy":
        """Deserialize XML element to EcucDestinationUriPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDestinationUriPolicy object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse containers (list)
        obj.containers = []
        for child in ARObject._find_all_child_elements(element, "CONTAINERS"):
            containers_value = ARObject._deserialize_by_tag(child, "EcucContainerDef")
            obj.containers.append(containers_value)

        # Parse destination_uri
        child = ARObject._find_child_element(element, "DESTINATION-URI")
        if child is not None:
            destination_uri_value = child.text
            obj.destination_uri = destination_uri_value

        # Parse parameters (list)
        obj.parameters = []
        for child in ARObject._find_all_child_elements(element, "PARAMETERS"):
            parameters_value = ARObject._deserialize_by_tag(child, "EcucParameterDef")
            obj.parameters.append(parameters_value)

        # Parse reference_refs (list)
        obj.reference_refs = []
        for child in ARObject._find_all_child_elements(element, "REFERENCES"):
            reference_refs_value = child.text
            obj.reference_refs.append(reference_refs_value)

        return obj



class EcucDestinationUriPolicyBuilder:
    """Builder for EcucDestinationUriPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDestinationUriPolicy = EcucDestinationUriPolicy()

    def build(self) -> EcucDestinationUriPolicy:
        """Build and return EcucDestinationUriPolicy object.

        Returns:
            EcucDestinationUriPolicy instance
        """
        # TODO: Add validation
        return self._obj
