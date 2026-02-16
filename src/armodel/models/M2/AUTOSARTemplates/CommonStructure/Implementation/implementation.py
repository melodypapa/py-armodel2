"""Implementation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RevisionLabelString,
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_manifest import (
    BuildActionManifest,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.code import (
    Code,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.compiler import (
    Compiler,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.dependency_on_artifact import (
    DependencyOnArtifact,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.linker import (
    Linker,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_support_data import (
    McSupportData,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.resource_consumption import (
    ResourceConsumption,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_mapping import (
    SwcBswMapping,
)


class Implementation(ARElement):
    """AUTOSAR Implementation."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("build_action_manifest", None, False, False, BuildActionManifest),  # buildActionManifest
        ("code_descriptors", None, False, True, Code),  # codeDescriptors
        ("compilers", None, False, True, Compiler),  # compilers
        ("generateds", None, False, True, DependencyOnArtifact),  # generateds
        ("hw_elements", None, False, True, HwElement),  # hwElements
        ("linkers", None, False, True, Linker),  # linkers
        ("mc_support", None, False, False, McSupportData),  # mcSupport
        ("programming", None, False, False, ProgramminglanguageEnum),  # programming
        ("required_artifacts", None, False, True, DependencyOnArtifact),  # requiredArtifacts
        ("requireds", None, False, True, DependencyOnArtifact),  # requireds
        ("resource", None, False, False, ResourceConsumption),  # resource
        ("swc_bsw", None, False, False, SwcBswMapping),  # swcBsw
        ("sw_version", None, True, False, None),  # swVersion
        ("used_code_generator", None, True, False, None),  # usedCodeGenerator
        ("vendor_id", None, True, False, None),  # vendorId
    ]

    def __init__(self) -> None:
        """Initialize Implementation."""
        super().__init__()
        self.build_action_manifest: Optional[BuildActionManifest] = None
        self.code_descriptors: list[Code] = []
        self.compilers: list[Compiler] = []
        self.generateds: list[DependencyOnArtifact] = []
        self.hw_elements: list[HwElement] = []
        self.linkers: list[Linker] = []
        self.mc_support: Optional[McSupportData] = None
        self.programming: Optional[ProgramminglanguageEnum] = None
        self.required_artifacts: list[DependencyOnArtifact] = []
        self.requireds: list[DependencyOnArtifact] = []
        self.resource: Optional[ResourceConsumption] = None
        self.swc_bsw: Optional[SwcBswMapping] = None
        self.sw_version: Optional[RevisionLabelString] = None
        self.used_code_generator: Optional[String] = None
        self.vendor_id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Implementation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Implementation":
        """Create Implementation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Implementation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Implementation since parent returns ARObject
        return cast("Implementation", obj)


class ImplementationBuilder:
    """Builder for Implementation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Implementation = Implementation()

    def build(self) -> Implementation:
        """Build and return Implementation object.

        Returns:
            Implementation instance
        """
        # TODO: Add validation
        return self._obj
